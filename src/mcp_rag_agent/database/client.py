"""Local Database Storage Engine for MCP RAG Agent.

Provides persistent, ACID-compliant local document storage, full-text lexical
search (via SQLite FTS5 with BM25), dense vector similarity search (via NumPy
cosine similarity), and Reciprocal Rank Fusion (RRF) hybrid search.
"""

from __future__ import annotations

import copy
import json
import logging
import math
import os
import re
import sqlite3
import threading
import time
import uuid
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Optional, Sequence, Union

import numpy as np

from mcp_rag_agent.observability import (
    ErrorCategory,
    get_current_tracer,
    get_request_id,
)

logger = logging.getLogger("LocalDatabaseClient")


class JSONCustomEncoder(json.JSONEncoder):
    """JSON Encoder that gracefully serializes dates, datetimes, UUIDs, and Enums."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if hasattr(obj, "value"):  # Enum
            return obj.value
        if hasattr(obj, "model_dump"):  # Pydantic v2
            return obj.model_dump(mode="json")
        if hasattr(obj, "dict"):  # Pydantic v1
            return obj.dict()
        return super().default(obj)


def _json_dumps(obj: Any) -> str:
    return json.dumps(obj, cls=JSONCustomEncoder, ensure_ascii=False)


def _json_loads(s: str) -> Any:
    return json.loads(s)


class InsertOneResult:
    """Result returned by insert_one."""

    def __init__(self, inserted_id: str) -> None:
        self.inserted_id = inserted_id

    def __repr__(self) -> str:
        return f"InsertOneResult(inserted_id={self.inserted_id!r})"


class InsertManyResult:
    """Result returned by insert_many."""

    def __init__(self, inserted_ids: list[str]) -> None:
        self.inserted_ids = inserted_ids

    def __repr__(self) -> str:
        return f"InsertManyResult(inserted_ids={self.inserted_ids!r})"


class UpdateResult:
    """Result returned by update_one."""

    def __init__(
        self, matched_count: int, modified_count: int, upserted_id: Optional[str] = None
    ) -> None:
        self.matched_count = matched_count
        self.modified_count = modified_count
        self.upserted_id = upserted_id

    def __repr__(self) -> str:
        return (
            f"UpdateResult(matched_count={self.matched_count}, "
            f"modified_count={self.modified_count}, upserted_id={self.upserted_id!r})"
        )


class DeleteResult:
    """Result returned by delete_one or delete_many."""

    def __init__(self, deleted_count: int) -> None:
        self.deleted_count = deleted_count

    def __repr__(self) -> str:
        return f"DeleteResult(deleted_count={self.deleted_count})"


def _get_nested_field(doc: dict[str, Any], path: str) -> Any:
    """Extract nested dictionary field using dot notation."""
    if "." not in path:
        return doc.get(path)
    parts = path.split(".")
    curr: Any = doc
    for part in parts:
        if isinstance(curr, dict):
            curr = curr.get(part)
        else:
            return None
    return curr


def _matches_filter(doc: dict[str, Any], query: Optional[dict[str, Any]]) -> bool:
    """Check if document matches a MongoDB-style query filter."""
    if not query:
        return True

    for key, expected in query.items():
        if key == "$text":
            search_term = str(expected.get("$search", "")).lower()
            content = str(doc.get("content", "")).lower()
            title = str(doc.get("title", "")).lower()
            if search_term:
                tokens = [t.strip() for t in search_term.split() if t.strip()]
                if not any(t in content or t in title for t in tokens):
                    return False
            continue

        val = _get_nested_field(doc, key)

        if isinstance(expected, dict):
            for op, op_val in expected.items():
                if op == "$in":
                    if isinstance(op_val, (list, tuple, set)):
                        val_cmp = (
                            val.value
                            if hasattr(val, "value")
                            else str(val)
                            if val is not None
                            else None
                        )
                        op_vals_cmp = [
                            v.value if hasattr(v, "value") else str(v) for v in op_val
                        ]
                        if val not in op_val and val_cmp not in op_vals_cmp:
                            return False
                    elif val != op_val:
                        return False
                elif op == "$gte":
                    if val is None or str(val) < str(op_val):
                        return False
                elif op == "$lte":
                    if val is None or str(val) > str(op_val):
                        return False
                elif op == "$gt":
                    if val is None or str(val) <= str(op_val):
                        return False
                elif op == "$lt":
                    if val is None or str(val) >= str(op_val):
                        return False
                elif op == "$ne":
                    if val == op_val:
                        return False
                elif op == "$regex":
                    if val is None or not re.search(str(op_val), str(val), re.IGNORECASE):
                        return False
        else:
            val_cmp = (
                val.value
                if hasattr(val, "value")
                else str(val)
                if val is not None
                else None
            )
            exp_cmp = (
                expected.value
                if hasattr(expected, "value")
                else str(expected)
                if expected is not None
                else None
            )
            if val != expected and val_cmp != exp_cmp:
                return False

    return True


def _apply_update(doc: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
    """Apply MongoDB update operators ($set, $push) to a document."""
    updated = copy.deepcopy(doc)
    if "$set" in update:
        for k, v in update["$set"].items():
            if "." in k:
                parts = k.split(".")
                target = updated
                for p in parts[:-1]:
                    if p not in target or not isinstance(target[p], dict):
                        target[p] = {}
                    target = target[p]
                target[parts[-1]] = v
            else:
                updated[k] = v

    if "$push" in update:
        for k, v in update["$push"].items():
            if k not in updated or not isinstance(updated[k], list):
                updated[k] = []
            updated[k].append(v)

    return updated


class LocalCursor:
    """Cursor-like iterator over retrieved local documents."""

    def __init__(self, documents: list[dict[str, Any]]) -> None:
        self._docs = list(documents)
        self._limit: Optional[int] = None
        self._sort_key: Optional[str] = None
        self._sort_direction: int = 1

    def limit(self, count: int) -> LocalCursor:
        self._limit = count
        return self

    def sort(self, key_or_list: Any, direction: int = 1) -> LocalCursor:
        if isinstance(key_or_list, list) and len(key_or_list) > 0:
            first = key_or_list[0]
            if isinstance(first, tuple):
                self._sort_key = first[0]
                self._sort_direction = first[1]
            else:
                self._sort_key = str(first)
                self._sort_direction = direction
        elif isinstance(key_or_list, str):
            self._sort_key = key_or_list
            self._sort_direction = direction
        return self

    def _get_items(self) -> list[dict[str, Any]]:
        docs = list(self._docs)
        if self._sort_key:
            reverse = self._sort_direction in (-1, "desc", "DESC")
            docs.sort(
                key=lambda d: str(d.get(self._sort_key) or ""),
                reverse=reverse,
            )
        if self._limit is not None:
            docs = docs[: self._limit]
        return docs

    def __iter__(self) -> Iterator[dict[str, Any]]:
        return iter(self._get_items())

    def __len__(self) -> int:
        return len(self._get_items())

    def __getitem__(self, index: Any) -> Any:
        return self._get_items()[index]


class LocalCollection:
    """Document collection interface backed by a SQLite table."""

    def __init__(self, client: LocalDatabaseClient, name: str) -> None:
        self._client = client
        self.name = name
        self._table_name = f"col_{self._clean_name(name)}"
        self._fts_table_name = f"fts_{self._clean_name(name)}"
        self._init_table()

    @staticmethod
    def _clean_name(name: str) -> str:
        return re.sub(r"[^a-zA-Z0-9_]", "_", name)

    def _init_table(self) -> None:
        with self._client._lock:
            conn = self._client._conn
            conn.execute(
                f"""CREATE TABLE IF NOT EXISTS {self._table_name} (
                    _id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );"""
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS _collections (name TEXT PRIMARY KEY);"
            )
            conn.execute(
                "INSERT OR IGNORE INTO _collections (name) VALUES (?);", (self.name,)
            )
            conn.commit()

    def _ensure_fts_table(self) -> None:
        with self._client._lock:
            conn = self._client._conn
            conn.execute(
                f"""CREATE VIRTUAL TABLE IF NOT EXISTS {self._fts_table_name} USING fts5(
                    doc_id UNINDEXED,
                    content,
                    tokenize='porter unicode61'
                );"""
            )
            # Backfill any existing documents that have content if FTS is empty
            count_cur = conn.execute(f"SELECT COUNT(*) FROM {self._fts_table_name};")
            if count_cur.fetchone()[0] == 0:
                cur = conn.execute(f"SELECT _id, data FROM {self._table_name};")
                rows = cur.fetchall()
                for did, raw_data in rows:
                    try:
                        parsed = _json_loads(raw_data)
                        if "content" in parsed and parsed["content"]:
                            conn.execute(
                                f"INSERT INTO {self._fts_table_name} (doc_id, content) VALUES (?, ?);",
                                (did, str(parsed["content"])),
                            )
                    except Exception:
                        pass
            conn.commit()

    def _has_fts_table(self) -> bool:
        with self._client._lock:
            cur = self._client._conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
                (self._fts_table_name,),
            )
            return cur.fetchone() is not None

    def insert_one(self, document: dict[str, Any]) -> InsertOneResult:
        doc = copy.deepcopy(document)
        doc_id = str(doc.get("_id") or doc.get("chunk_id") or doc.get("ticket_id") or doc.get("incident_id") or doc.get("device_id") or doc.get("user_id") or doc.get("approval_id") or doc.get("event_id") or doc.get("document_id") or uuid.uuid4().hex)
        doc["_id"] = doc_id
        payload = _json_dumps(doc)

        has_content = "content" in doc and doc["content"]
        if has_content:
            self._ensure_fts_table()

        with self._client._lock:
            conn = self._client._conn
            conn.execute(
                f"INSERT OR REPLACE INTO {self._table_name} (_id, data, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP);",
                (doc_id, payload),
            )
            if has_content:
                content_text = str(doc.get("content") or "")
                conn.execute(
                    f"DELETE FROM {self._fts_table_name} WHERE doc_id = ?;", (doc_id,)
                )
                conn.execute(
                    f"INSERT INTO {self._fts_table_name} (doc_id, content) VALUES (?, ?);",
                    (doc_id, content_text),
                )
            conn.commit()

        return InsertOneResult(doc_id)

    def insert_many(self, documents: Sequence[dict[str, Any]]) -> InsertManyResult:
        inserted_ids: list[str] = []
        any_content = any("content" in d and d.get("content") for d in documents)
        if any_content:
            self._ensure_fts_table()

        with self._client._lock:
            conn = self._client._conn
            has_fts = self._has_fts_table()
            for document in documents:
                doc = copy.deepcopy(document)
                doc_id = str(doc.get("_id") or doc.get("chunk_id") or doc.get("document_id") or uuid.uuid4().hex)
                doc["_id"] = doc_id
                payload = _json_dumps(doc)
                conn.execute(
                    f"INSERT OR REPLACE INTO {self._table_name} (_id, data, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP);",
                    (doc_id, payload),
                )
                if has_fts and "content" in doc and doc.get("content"):
                    content_text = str(doc.get("content") or "")
                    conn.execute(
                        f"DELETE FROM {self._fts_table_name} WHERE doc_id = ?;",
                        (doc_id,),
                    )
                    conn.execute(
                        f"INSERT INTO {self._fts_table_name} (doc_id, content) VALUES (?, ?);",
                        (doc_id, content_text),
                    )
                inserted_ids.append(doc_id)
            conn.commit()

        return InsertManyResult(inserted_ids)

    def find_one(self, query: Optional[dict[str, Any]] = None) -> Optional[dict[str, Any]]:
        cursor = self.find(query).limit(1)
        items = list(cursor)
        return items[0] if items else None

    def find(self, query: Optional[dict[str, Any]] = None) -> LocalCursor:
        with self._client._lock:
            cur = self._client._conn.execute(f"SELECT data FROM {self._table_name};")
            rows = cur.fetchall()

        matched: list[dict[str, Any]] = []
        for (data_json,) in rows:
            doc = _json_loads(data_json)
            if _matches_filter(doc, query):
                matched.append(doc)

        return LocalCursor(matched)

    def update_one(
        self,
        query: dict[str, Any],
        update: dict[str, Any],
        upsert: bool = False,
    ) -> UpdateResult:
        doc = self.find_one(query)
        if doc is not None:
            updated_doc = _apply_update(doc, update)
            doc_id = str(updated_doc["_id"])
            payload = _json_dumps(updated_doc)
            with self._client._lock:
                conn = self._client._conn
                conn.execute(
                    f"UPDATE {self._table_name} SET data = ?, updated_at = CURRENT_TIMESTAMP WHERE _id = ?;",
                    (payload, doc_id),
                )
                if self._has_fts_table() and "content" in updated_doc:
                    conn.execute(
                        f"DELETE FROM {self._fts_table_name} WHERE doc_id = ?;",
                        (doc_id,),
                    )
                    conn.execute(
                        f"INSERT INTO {self._fts_table_name} (doc_id, content) VALUES (?, ?);",
                        (doc_id, str(updated_doc.get("content") or "")),
                    )
                conn.commit()
            return UpdateResult(matched_count=1, modified_count=1)

        if upsert:
            new_doc = copy.deepcopy(query)
            if "$set" in update:
                new_doc = _apply_update(new_doc, {"$set": update["$set"]})
            if "$push" in update:
                new_doc = _apply_update(new_doc, {"$push": update["$push"]})
            res = self.insert_one(new_doc)
            return UpdateResult(matched_count=0, modified_count=1, upserted_id=res.inserted_id)

        return UpdateResult(matched_count=0, modified_count=0)

    def delete_one(self, query: dict[str, Any]) -> DeleteResult:
        doc = self.find_one(query)
        if doc is None:
            return DeleteResult(deleted_count=0)
        doc_id = str(doc["_id"])
        with self._client._lock:
            conn = self._client._conn
            conn.execute(f"DELETE FROM {self._table_name} WHERE _id = ?;", (doc_id,))
            if self._has_fts_table():
                conn.execute(
                    f"DELETE FROM {self._fts_table_name} WHERE doc_id = ?;", (doc_id,)
                )
            conn.commit()
        return DeleteResult(deleted_count=1)

    def delete_many(self, query: dict[str, Any]) -> DeleteResult:
        docs = list(self.find(query))
        if not docs:
            return DeleteResult(deleted_count=0)

        deleted = len(docs)
        with self._client._lock:
            conn = self._client._conn
            for doc in docs:
                doc_id = str(doc["_id"])
                conn.execute(f"DELETE FROM {self._table_name} WHERE _id = ?;", (doc_id,))
                if self._has_fts_table():
                    conn.execute(
                        f"DELETE FROM {self._fts_table_name} WHERE doc_id = ?;",
                        (doc_id,),
                    )
            conn.commit()

        return DeleteResult(deleted_count=deleted)

    def create_index(self, keys: Any, **kwargs: Any) -> None:
        """Create or ensure index. Automatically manages FTS5 virtual tables."""
        if kwargs.get("weights") or (isinstance(keys, list) and any(k[1] == "text" for k in keys if isinstance(k, tuple))):
            self._ensure_fts_table()

    def create_search_index(self, definition: dict[str, Any]) -> None:
        """Manage vector or search index metadata."""
        if definition.get("type") == "vectorSearch":
            pass  # NumPy handles dense vector scoring
        else:
            self._ensure_fts_table()

    def aggregate(self, pipeline: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Evaluate aggregation pipeline stages ($match, $limit, $sort, $addFields)."""
        docs = list(self.find())
        for stage in pipeline:
            if "$match" in stage:
                docs = [d for d in docs if _matches_filter(d, stage["$match"])]
            elif "$sort" in stage:
                sort_spec = stage["$sort"]
                for k, direction in sort_spec.items():
                    reverse = direction in (-1, "desc", "DESC")
                    docs.sort(key=lambda d: d.get(k) or 0, reverse=reverse)
            elif "$limit" in stage:
                docs = docs[: stage["$limit"]]
            elif "$addFields" in stage:
                for k, v in stage["$addFields"].items():
                    for d in docs:
                        if isinstance(v, dict) and "$meta" in v:
                            pass
                        else:
                            d[k] = v
        return docs

    def count_documents(self, query: Optional[dict[str, Any]] = None) -> int:
        return len(self.find(query))


class AdminCommandWrapper:
    """Wrapper emulating MongoDB admin commands for health checks."""

    def command(self, cmd: str, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return {"ok": 1.0, "status": "healthy"}


class LocalDatabaseClient:
    """Unified local database storage client replacing MongoDB.

    Features:
    - Pure local SQLite persistence (WAL mode, zero server daemon).
    - Full-text search via SQLite FTS5 (BM25 ranking and stemming).
    - Dense vector search via NumPy (exact cosine similarity).
    - Reciprocal Rank Fusion (RRF) hybrid search.
    - 100% backward-compatible API contracts with existing stores and tools.
    """

    def __init__(
        self,
        db_path: Optional[str] = None,
        uri: Optional[str] = None,
        database_name: Optional[str] = None,
        database_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize LocalDatabaseClient.

        Args:
            db_path: Path to the SQLite database file.
            uri: Legacy parameter preserved for backward compatibility.
            database_name: Legacy parameter preserved for backward compatibility.
            database_path: Alias for db_path.
        """
        # Determine actual file path
        resolved_path: str
        effective_path = db_path or database_path
        if effective_path:
            resolved_path = effective_path
        elif uri and (uri.startswith("sqlite:///") or uri.endswith(".db")):
            resolved_path = uri.replace("sqlite:///", "")
        elif uri and not uri.startswith("mongodb"):
            resolved_path = uri
        else:
            resolved_path = os.environ.get("LOCAL_DB_PATH", "./data/local_storage.db")

        # Handle special :memory: mode
        if resolved_path == ":memory:":
            self._db_path = ":memory:"
        else:
            target_path = Path(resolved_path).resolve()
            target_path.parent.mkdir(parents=True, exist_ok=True)
            self._db_path = str(target_path)

        self._database_name = database_name or "local_storage"
        self._uri = uri or self._db_path
        self._conn: Optional[sqlite3.Connection] = None
        self._collections: dict[str, LocalCollection] = {}
        self._lock = threading.RLock()

    def connect(self) -> None:
        """Establish local database connection with WAL mode and busy timeout."""
        with self._lock:
            if self._conn is not None:
                return

            t0 = time.perf_counter()
            req_id = get_request_id() or "-"
            tracer = get_current_tracer()

            try:
                self._conn = sqlite3.connect(
                    self._db_path,
                    check_same_thread=False,
                    timeout=10.0,
                )
                # Configure SQLite performance and concurrency
                if self._db_path != ":memory:":
                    self._conn.execute("PRAGMA journal_mode = WAL;")
                self._conn.execute("PRAGMA busy_timeout = 5000;")
                self._conn.execute("PRAGMA foreign_keys = ON;")

                # Metadata table
                self._conn.execute(
                    "CREATE TABLE IF NOT EXISTS _collections (name TEXT PRIMARY KEY);"
                )
                self._conn.commit()

                elapsed = (time.perf_counter() - t0) * 1000.0
                logger.debug(
                    f"[req:{req_id}] Connected to local database: {self._db_path} ({elapsed:.1f}ms)"
                )
                if tracer:
                    tracer.record_database_op(
                        "connect", self._database_name, elapsed, "success"
                    )
            except Exception as e:
                elapsed = (time.perf_counter() - t0) * 1000.0
                logger.error(f"[req:{req_id}] Failed to connect to local database: {e}")
                if tracer:
                    tracer.record_error(
                        category=ErrorCategory.DATABASE_ERROR,
                        message=f"Failed to connect to local database: {e}",
                        details={"database": self._database_name, "path": self._db_path},
                        exc=e,
                        recoverable=False,
                    )
                raise

    def disconnect(self) -> None:
        """Close local database connection."""
        with self._lock:
            if self._conn is not None:
                try:
                    self._conn.close()
                except Exception:
                    pass
                self._conn = None
                self._collections.clear()

    @property
    def db(self) -> LocalDatabaseClient:
        """Property returning self for MongoClient.db compatibility."""
        if self._conn is None:
            self.connect()
        return self

    @property
    def admin(self) -> AdminCommandWrapper:
        """Admin property supporting client.admin.command('ping')."""
        return AdminCommandWrapper()

    def ping(self) -> dict[str, Any]:
        """Perform health check verification on the local database."""
        if self._conn is None:
            self.connect()
        with self._lock:
            cur = self._conn.execute("SELECT 1;")
            assert cur.fetchone()[0] == 1
        return {"ok": 1.0, "status": "healthy"}

    def get_collection(self, collection_name: str) -> LocalCollection:
        """Retrieve or create a LocalCollection adapter by name."""
        if self._conn is None:
            self.connect()
        with self._lock:
            if collection_name not in self._collections:
                self._collections[collection_name] = LocalCollection(self, collection_name)
            return self._collections[collection_name]

    def __getitem__(self, collection_name: str) -> LocalCollection:
        """Allow client['collection_name'] syntax."""
        return self.get_collection(collection_name)

    def list_collections(self) -> list[str]:
        """List all collection names in the local database."""
        if self._conn is None:
            self.connect()
        with self._lock:
            cur = self._conn.execute("SELECT name FROM _collections ORDER BY name;")
            return [row[0] for row in cur.fetchall()]

    def list_collection_names(self) -> list[str]:
        return self.list_collections()

    def create_collection(self, collection_name: str) -> LocalCollection:
        return self.get_collection(collection_name)

    def collection_exists(self, collection_name: str) -> bool:
        return collection_name in self.list_collections()

    def drop_collection(self, collection_name: str) -> bool:
        """Drop a collection and its associated tables."""
        if self._conn is None:
            self.connect()
        tbl = f"col_{LocalCollection._clean_name(collection_name)}"
        fts_tbl = f"fts_{LocalCollection._clean_name(collection_name)}"
        with self._lock:
            self._conn.execute(f"DROP TABLE IF EXISTS {tbl};")
            self._conn.execute(f"DROP TABLE IF EXISTS {fts_tbl};")
            self._conn.execute(
                "DELETE FROM _collections WHERE name = ?;", (collection_name,)
            )
            self._conn.commit()
            self._collections.pop(collection_name, None)
        return True

    def drop_database(self, database_name: Optional[str] = None) -> None:
        """Drop all collections in the database."""
        for col_name in list(self.list_collections()):
            self.drop_collection(col_name)

    def insert_document(self, collection_name: str, document: dict[str, Any]) -> str:
        col = self.get_collection(collection_name)
        result = col.insert_one(document)
        return result.inserted_id

    def insert_documents(
        self, collection_name: str, documents: list[dict[str, Any]]
    ) -> list[str]:
        col = self.get_collection(collection_name)
        result = col.insert_many(documents)
        return result.inserted_ids

    def find_document(
        self, collection_name: str, query: dict[str, Any]
    ) -> Optional[dict[str, Any]]:
        col = self.get_collection(collection_name)
        return col.find_one(query)

    def find_documents(
        self, collection_name: str, query: dict[str, Any], limit: int = 10
    ) -> list[dict[str, Any]]:
        col = self.get_collection(collection_name)
        return list(col.find(query).limit(limit))

    def delete_documents(self, collection_name: str, query: dict[str, Any]) -> int:
        col = self.get_collection(collection_name)
        result = col.delete_many(query)
        return result.deleted_count

    def create_vector_search_index(
        self,
        collection_name: str,
        index_name: str,
        vector_field: str,
        dimensions: int,
        similarity: str = "cosine",
    ) -> None:
        """Record vector search index metadata."""
        col = self.get_collection(collection_name)
        col.create_search_index(
            {
                "name": index_name,
                "type": "vectorSearch",
                "definition": {
                    "fields": [
                        {
                            "type": "vector",
                            "path": vector_field,
                            "numDimensions": dimensions,
                            "similarity": similarity,
                        }
                    ]
                },
            }
        )

    def create_text_search_index(
        self,
        collection_name: str,
        index_name: str,
        text_fields: list[str],
        weights: Optional[dict[str, int]] = None,
    ) -> None:
        """Initialize FTS5 virtual table for full-text search on collection."""
        col = self.get_collection(collection_name)
        col._ensure_fts_table()

    def vector_search(
        self,
        collection_name: str,
        index_name: str = "vector_index",
        vector_field: str = "embedding",
        query_vector: Optional[list[float]] = None,
        limit: int = 10,
        num_candidates: int = 100,
        filter_query: Optional[dict[str, Any]] = None,
        min_score: Optional[float] = None,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Perform dense vector similarity search using exact NumPy cosine similarity."""
        t0 = time.perf_counter()
        tracer = get_current_tracer()
        req_id = get_request_id() or "-"

        try:
            col = self.get_collection(collection_name)
            candidate_docs = list(col.find(filter_query))

            if not candidate_docs or not query_vector:
                return []

            q_vec = np.array(query_vector, dtype=np.float32)
            q_norm = float(np.linalg.norm(q_vec))
            if q_norm == 0.0:
                q_norm = 1.0

            scored_docs: list[dict[str, Any]] = []
            for doc in candidate_docs:
                vec = doc.get(vector_field)
                if not vec or not isinstance(vec, (list, tuple)):
                    continue
                v_arr = np.array(vec, dtype=np.float32)
                v_norm = float(np.linalg.norm(v_arr))
                if v_norm == 0.0:
                    sim = 0.0
                else:
                    sim = float(np.dot(q_vec, v_arr) / (q_norm * v_norm))

                if min_score is not None and sim < min_score:
                    continue

                res_doc = copy.deepcopy(doc)
                res_doc["score"] = round(sim, 6)
                scored_docs.append(res_doc)

            scored_docs.sort(key=lambda x: x["score"], reverse=True)
            results = scored_docs[:limit]

            elapsed = (time.perf_counter() - t0) * 1000.0
            if tracer:
                tracer.record_database_op(
                    "vector_search",
                    collection_name,
                    elapsed,
                    "success",
                    {"candidates": len(results)},
                )
            return results

        except Exception as e:
            elapsed = (time.perf_counter() - t0) * 1000.0
            logger.error(f"[req:{req_id}] Local vector search failed: {e}")
            if tracer:
                tracer.record_error(
                    category=ErrorCategory.DATABASE_ERROR,
                    message=f"Local vector search failed: {e}",
                    details={"collection": collection_name, "index": index_name},
                    exc=e,
                    recoverable=False,
                )
            raise

    def text_search(
        self,
        collection_name: str,
        index_name: str = "text_index",
        query_text: str = "",
        limit: int = 10,
        filter_query: Optional[dict[str, Any]] = None,
        use_atlas_search: bool = False,
        min_score: Optional[float] = None,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Perform full-text lexical search using SQLite FTS5 with BM25 ranking."""
        t0 = time.perf_counter()
        tracer = get_current_tracer()
        req_id = get_request_id() or "-"

        try:
            col = self.get_collection(collection_name)
            col._ensure_fts_table()

            tokens = re.findall(r"\b\w+\b", query_text.lower())
            if not tokens:
                return []

            fts_q = " OR ".join(f'"{t}"*' for t in tokens)

            with self._lock:
                cur = self._conn.execute(
                    f"SELECT doc_id, bm25({col._fts_table_name}) as bm25_score "
                    f"FROM {col._fts_table_name} WHERE {col._fts_table_name} MATCH ? "
                    f"ORDER BY bm25_score LIMIT ?;",
                    (fts_q, limit * 3),
                )
                fts_rows = cur.fetchall()

            results: list[dict[str, Any]] = []
            for doc_id, bm25_score in fts_rows:
                doc = col.find_one({"_id": doc_id})
                if not doc:
                    continue
                if filter_query and not _matches_filter(doc, filter_query):
                    continue

                score = round(abs(float(bm25_score)) * 10.0 + 1.0, 4)
                if min_score is not None and score < min_score:
                    continue

                res_doc = copy.deepcopy(doc)
                res_doc["text_score"] = score
                results.append(res_doc)

            results.sort(key=lambda x: x["text_score"], reverse=True)
            results = results[:limit]

            elapsed = (time.perf_counter() - t0) * 1000.0
            if tracer:
                tracer.record_database_op(
                    "text_search",
                    collection_name,
                    elapsed,
                    "success",
                    {"matches": len(results)},
                )
            return results

        except Exception as e:
            elapsed = (time.perf_counter() - t0) * 1000.0
            logger.error(f"[req:{req_id}] Local text search failed: {e}")
            if tracer:
                tracer.record_error(
                    category=ErrorCategory.DATABASE_ERROR,
                    message=f"Local text search failed: {e}",
                    details={"collection": collection_name, "index": index_name},
                    exc=e,
                    recoverable=False,
                )
            raise

    def hybrid_search(
        self,
        collection_name: str,
        vector_index_name: str = "vector_index",
        text_index_name: str = "text_index",
        vector_field: str = "embedding",
        query_vector: Optional[list[float]] = None,
        query_text: str = "",
        limit: int = 10,
        num_candidates: int = 100,
        semantic_weight: float = 0.7,
        filter_query: Optional[dict[str, Any]] = None,
        rrf_k: int = 60,
        min_vector_score: Optional[float] = None,
        min_text_score: Optional[float] = None,
        min_rrf_score: Optional[float] = None,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Combine dense vector search and FTS5 keyword search using Reciprocal Rank Fusion (RRF)."""
        vector_weight = semantic_weight
        text_weight = 1.0 - semantic_weight

        # 1. Fetch vector candidates
        vector_results = self.vector_search(
            collection_name=collection_name,
            index_name=vector_index_name,
            vector_field=vector_field,
            query_vector=query_vector,
            limit=limit * 2,
            num_candidates=num_candidates,
            filter_query=filter_query,
            min_score=min_vector_score,
        )

        # 2. Fetch text candidates
        text_results = self.text_search(
            collection_name=collection_name,
            index_name=text_index_name,
            query_text=query_text,
            limit=limit * 2,
            filter_query=filter_query,
            min_score=min_text_score,
        )

        # 3. Reciprocal Rank Fusion (RRF)
        rrf_scores: dict[str, dict[str, Any]] = {}

        for rank, doc in enumerate(vector_results, start=1):
            doc_id = str(doc["_id"])
            rrf_score = vector_weight / (rrf_k + rank)
            rrf_scores[doc_id] = {
                "document": doc,
                "rrf_score": rrf_score,
                "vector_rank": rank,
                "vector_score": doc.get("score"),
                "text_rank": None,
                "text_score": None,
            }

        for rank, doc in enumerate(text_results, start=1):
            doc_id = str(doc["_id"])
            rrf_score = text_weight / (rrf_k + rank)
            if doc_id in rrf_scores:
                rrf_scores[doc_id]["rrf_score"] += rrf_score
                rrf_scores[doc_id]["text_rank"] = rank
                rrf_scores[doc_id]["text_score"] = doc.get("text_score")
            else:
                rrf_scores[doc_id] = {
                    "document": doc,
                    "rrf_score": rrf_score,
                    "vector_rank": None,
                    "vector_score": None,
                    "text_rank": rank,
                    "text_score": doc.get("text_score"),
                }

        # 4. Sort descending by RRF score
        sorted_results = sorted(
            rrf_scores.values(), key=lambda x: x["rrf_score"], reverse=True
        )

        # 5. Build final result list
        final_results = []
        for item in sorted_results[:limit]:
            if min_rrf_score is not None and item["rrf_score"] < min_rrf_score:
                continue

            doc = copy.deepcopy(item["document"])
            doc["rrf_score"] = round(item["rrf_score"], 6)
            doc["vector_rank"] = item["vector_rank"]
            doc["text_rank"] = item["text_rank"]
            if item["vector_score"] is not None:
                doc["vector_score"] = item["vector_score"]
            if item["text_score"] is not None:
                doc["text_score"] = item["text_score"]

            final_results.append(doc)

        return final_results

    def ping(self) -> bool:
        """Ping database connection to verify connectivity and readiness."""
        try:
            if self._conn is None:
                self.connect()
            with self._lock:
                if self._conn is not None:
                    cur = self._conn.execute("SELECT 1;")
                    return cur.fetchone() is not None
            return False
        except Exception:
            return False
