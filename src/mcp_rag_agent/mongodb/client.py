"""MongoDB client wrapper with dual-mode support: MongoDB Atlas or Local Database Storage.

When configured with a MongoDB URI (e.g. mongodb:// or mongodb+srv://), this client communicates
with MongoDB Atlas using PyMongo. When configured without a MongoDB URI or for local operations,
it transparently delegates to LocalDatabaseClient (SQLite + FTS5 BM25 + NumPy vector cosine similarity),
allowing the entire project to operate completely offline and serverless without requiring MongoDB.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Optional

try:
    from pymongo import MongoClient
    from pymongo.collection import Collection
    from pymongo.database import Database
except ImportError:
    class MongoClient:  # type: ignore
        pass

    class Collection:  # type: ignore
        pass

    class Database:  # type: ignore
        pass

from mcp_rag_agent.database.client import (
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    LocalCollection,
    LocalCursor,
    LocalDatabaseClient,
    UpdateResult,
)
from mcp_rag_agent.observability import (
    ErrorCategory,
    get_current_tracer,
    get_request_id,
)

logger = logging.getLogger("MongoDBClient")


class MongoDBClient:
    """MongoDB client wrapper supporting both MongoDB Atlas and Local SQLite storage."""

    def __init__(
        self,
        uri: Optional[str] = None,
        database_name: Optional[str] = None,
        db_path: Optional[str] = None,
    ) -> None:
        """Initialize database client.

        Args:
            uri: MongoDB connection URI or local database path.
            database_name: Name of the database to use.
            db_path: Optional explicit local SQLite database file path.
        """
        self._uri = uri or ""
        self._database_name = database_name or "local_storage"
        self._client: Optional[MongoClient] = None
        self._db: Optional[Database] = None

        self._is_mongo = self._uri.startswith("mongodb://") or self._uri.startswith("mongodb+srv://")

        if not self._is_mongo:
            resolved_path = db_path or (
                self._uri if self._uri and not self._uri.startswith("sqlite://") else "./data/local_storage.db"
            )
            if resolved_path.startswith("sqlite:///"):
                resolved_path = resolved_path.replace("sqlite:///", "")
            self._local_client = LocalDatabaseClient(database_path=resolved_path)
        else:
            self._local_client = None

    @property
    def is_local(self) -> bool:
        """Check if client is running in local SQLite mode."""
        return not self._is_mongo

    def connect(self) -> None:
        """Establish connection to MongoDB or initialize local database."""
        if not self._is_mongo:
            if self._local_client:
                self._local_client.connect()
            return

        if not self._uri:
            raise ValueError(
                "MongoDB connection URI cannot be empty. "
                "Please configure MONGODB_ATLAS_CLUSTER_URI in your environment or .env file."
            )
        if not self._database_name:
            raise ValueError(
                "MongoDB database name cannot be empty. "
                "Please configure MONGODB_ATLAS_DB_NAME in your environment or .env file."
            )

        if self._client is None:
            t0 = time.perf_counter()
            req_id = get_request_id() or "-"
            tracer = get_current_tracer()
            try:
                self._client = MongoClient(self._uri)
                self._db = self._client[self._database_name]
                elapsed = (time.perf_counter() - t0) * 1000.0
                logger.debug(
                    f"[req:{req_id}] Connected to MongoDB database: {self._database_name} ({elapsed:.1f}ms)"
                )
                if tracer:
                    tracer.record_database_op(
                        "connect", self._database_name, elapsed, "success"
                    )
            except Exception as e:
                elapsed = (time.perf_counter() - t0) * 1000.0
                logger.error(f"[req:{req_id}] Failed to connect to MongoDB: {e}")
                if tracer:
                    tracer.record_error(
                        category=ErrorCategory.DATABASE_ERROR,
                        message=f"Failed to connect to MongoDB: {e}",
                        details={"database": self._database_name},
                        exc=e,
                        recoverable=False,
                    )
                raise

    def disconnect(self) -> None:
        """Close database connection."""
        if not self._is_mongo:
            if self._local_client:
                self._local_client.disconnect()
            return

        if self._client:
            self._client.close()
            self._client = None
            self._db = None

    @property
    def db(self) -> Any:
        """Get the database instance."""
        if not self._is_mongo:
            return self._local_client
        if self._db is None:
            self.connect()
        return self._db

    def get_collection(self, collection_name: str) -> Any:
        """Get a collection by name."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.get_collection(collection_name)
        return self.db[collection_name]

    def list_collections(self) -> list[str]:
        """List all collections in the database."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.list_collections()
        return self.db.list_collection_names()

    def create_collection(self, collection_name: str) -> Any:
        """Create a new collection in the database."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.create_collection(collection_name)
        return self.db.create_collection(collection_name)

    def collection_exists(self, collection_name: str) -> bool:
        """Check if a collection exists in the database."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.collection_exists(collection_name)
        return collection_name in self.list_collections()

    def insert_document(self, collection_name: str, document: dict[str, Any]) -> str:
        """Insert a document into a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.insert_document(collection_name, document)
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return str(result.inserted_id)

    def insert_documents(
        self, collection_name: str, documents: list[dict[str, Any]]
    ) -> list[str]:
        """Insert multiple documents into a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.insert_documents(collection_name, documents)
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        return [str(id_) for id_ in result.inserted_ids]

    def find_document(
        self, collection_name: str, query: Optional[dict[str, Any]] = None
    ) -> Optional[dict[str, Any]]:
        """Find a single document in a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.find_document(collection_name, query or {})
        collection = self.get_collection(collection_name)
        return collection.find_one(query or {})

    def find_documents(
        self,
        collection_name: str,
        query: Optional[dict[str, Any]] = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Find documents in a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.find_documents(collection_name, query, limit)
        collection = self.get_collection(collection_name)
        cursor = collection.find(query or {}).limit(limit)
        return list(cursor)

    def delete_documents(
        self, collection_name: str, query: Optional[dict[str, Any]] = None
    ) -> int:
        """Delete documents from a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.delete_documents(collection_name, query or {})
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query or {})
        return result.deleted_count

    def create_vector_search_index(
        self,
        collection_name: str,
        index_name: str,
        vector_field: str,
        dimensions: int,
        similarity: str = "cosine",
    ) -> None:
        """Create a vector search index on a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.create_vector_search_index(
                collection_name, index_name, vector_field, dimensions, similarity
            )
        collection = self.get_collection(collection_name)
        index_definition = {
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
        collection.create_search_index(index_definition)

    def create_text_search_index(
        self, collection_name: str, index_name: str, text_fields: list[str]
    ) -> None:
        """Create a text search index on a collection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.create_text_search_index(
                collection_name, index_name, text_fields
            )
        collection = self.get_collection(collection_name)
        index_fields = [(field, "text") for field in text_fields]
        collection.create_index(index_fields, name=index_name)

    def vector_search(
        self,
        collection_name: str,
        index_name: str,
        vector_field: str,
        query_vector: list[float],
        limit: int = 10,
        num_candidates: int = 100,
        filter_query: Optional[dict[str, Any]] = None,
        min_score: Optional[float] = None,
    ) -> list[dict[str, Any]]:
        """Perform vector similarity search."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.vector_search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=limit,
                filter_query=filter_query,
                min_score=min_score,
                vector_field=vector_field,
                index_name=index_name,
            )

        collection = self.get_collection(collection_name)
        t0 = time.perf_counter()
        tracer = get_current_tracer()
        req_id = get_request_id() or "-"

        pipeline = [
            {
                "$vectorSearch": {
                    "index": index_name,
                    "path": vector_field,
                    "queryVector": query_vector,
                    "numCandidates": num_candidates,
                    "limit": limit,
                }
            },
            {"$addFields": {"score": {"$meta": "vectorSearchScore"}}},
        ]

        if filter_query:
            pipeline[0]["$vectorSearch"]["filter"] = filter_query

        try:
            results = list(collection.aggregate(pipeline))
            if min_score is not None:
                results = [doc for doc in results if doc.get("score", 0) >= min_score]
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
            logger.error(f"[req:{req_id}] MongoDB vector search failed: {e}")
            if tracer:
                tracer.record_error(
                    category=ErrorCategory.DATABASE_ERROR,
                    message=f"MongoDB vector search failed: {e}",
                    details={"collection": collection_name, "index": index_name},
                    exc=e,
                    recoverable=False,
                )
            raise

    def text_search(
        self,
        collection_name: str,
        index_name: str,
        query_text: str,
        limit: int = 10,
        filter_query: Optional[dict[str, Any]] = None,
        use_atlas_search: bool = False,
        min_score: Optional[float] = None,
    ) -> list[dict[str, Any]]:
        """Perform full-text search."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.text_search(
                collection_name=collection_name,
                query_text=query_text,
                limit=limit,
                filter_query=filter_query,
                min_score=min_score,
                index_name=index_name,
            )

        collection = self.get_collection(collection_name)
        t0 = time.perf_counter()
        tracer = get_current_tracer()
        req_id = get_request_id() or "-"

        try:
            match_stage: dict[str, Any] = {"$text": {"$search": query_text}}
            if filter_query:
                match_stage.update(filter_query)

            pipeline: list[dict[str, Any]] = [
                {"$match": match_stage},
                {"$addFields": {"text_score": {"$meta": "textScore"}}},
                {"$sort": {"text_score": -1}},
                {"$limit": limit},
            ]

            results = list(collection.aggregate(pipeline))
            if min_score is not None:
                results = [doc for doc in results if doc.get("text_score", 0) >= min_score]

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
            logger.error(f"[req:{req_id}] MongoDB text search failed: {e}")
            if tracer:
                tracer.record_error(
                    category=ErrorCategory.DATABASE_ERROR,
                    message=f"MongoDB text search failed: {e}",
                    details={"collection": collection_name, "index": index_name},
                    exc=e,
                    recoverable=False,
                )
            raise

    def hybrid_search(
        self,
        collection_name: str,
        vector_index_name: str,
        text_index_name: str,
        vector_field: str,
        query_vector: list[float],
        query_text: str,
        limit: int = 10,
        semantic_weight: float = 0.7,
        num_candidates: int = 100,
        filter_query: Optional[dict[str, Any]] = None,
        rrf_k: int = 60,
        min_vector_score: Optional[float] = None,
        min_text_score: Optional[float] = None,
        min_rrf_score: Optional[float] = None,
    ) -> list[dict[str, Any]]:
        """Perform hybrid search combining vector and text search using RRF."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.hybrid_search(
                collection_name=collection_name,
                query_vector=query_vector,
                query_text=query_text,
                limit=limit,
                semantic_weight=semantic_weight,
                filter_query=filter_query,
                rrf_k=rrf_k,
                min_vector_score=min_vector_score,
                min_text_score=min_text_score,
                min_rrf_score=min_rrf_score,
                vector_field=vector_field,
            )

        vector_weight = semantic_weight
        text_weight = 1.0 - semantic_weight

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

        text_results = self.text_search(
            collection_name=collection_name,
            index_name=text_index_name,
            query_text=query_text,
            limit=limit * 2,
            filter_query=filter_query,
            min_score=min_text_score,
        )

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

        sorted_results = sorted(
            rrf_scores.values(), key=lambda x: x["rrf_score"], reverse=True
        )

        final_results = []
        for item in sorted_results[:limit]:
            if min_rrf_score is not None and item["rrf_score"] < min_rrf_score:
                continue

            doc = item["document"]
            doc["rrf_score"] = item["rrf_score"]
            doc["vector_rank"] = item["vector_rank"]
            doc["text_rank"] = item["text_rank"]

            if item["vector_score"] is not None:
                doc["vector_score"] = item["vector_score"]
            if item["text_score"] is not None:
                doc["text_score"] = item["text_score"]

            final_results.append(doc)

        return final_results

    def ping(self) -> bool:
        """Ping database connection."""
        if not self._is_mongo:
            assert self._local_client is not None
            return self._local_client.ping()
        try:
            if self._client is None:
                self.connect()
            assert self._client is not None
            self._client.admin.command("ping")
            return True
        except Exception:
            return False
