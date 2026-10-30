import asyncio
import logging
import os
import sqlite3
from typing import Optional

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import MemorySaver

try:
    from langgraph.checkpoint.sqlite import SqliteSaver

    class CompatibleSqliteSaver(SqliteSaver):
        """SqliteSaver subclass that bridges sync SQLite operations into async methods for LangGraph."""

        async def aget_tuple(self, config):
            return await asyncio.to_thread(self.get_tuple, config)

        async def aget(self, config):
            return await asyncio.to_thread(self.get, config)

        async def aput(self, config, checkpoint, metadata, new_versions):
            cfg = dict(config)
            if "configurable" in cfg:
                cfg["configurable"] = dict(cfg["configurable"])
                cfg["configurable"].setdefault("checkpoint_ns", "")
            return await asyncio.to_thread(
                self.put, cfg, checkpoint, metadata, new_versions
            )

        async def aput_writes(self, config, writes, task_id):
            cfg = dict(config)
            if "configurable" in cfg:
                cfg["configurable"] = dict(cfg["configurable"])
                cfg["configurable"].setdefault("checkpoint_ns", "")
            return await asyncio.to_thread(self.put_writes, cfg, writes, task_id)

        async def alist(self, config, *, filter=None, before=None, limit=None):
            items = await asyncio.to_thread(
                lambda: list(
                    self.list(config, filter=filter, before=before, limit=limit)
                )
            )
            for item in items:
                yield item

except ImportError:
    SqliteSaver = None  # type: ignore
    CompatibleSqliteSaver = None  # type: ignore

try:
    from langgraph.checkpoint.mongodb import MongoDBSaver
    from pymongo import MongoClient
except ImportError:
    MongoDBSaver = None  # type: ignore
    MongoClient = None  # type: ignore

from mcp_rag_agent.core.config import Config, config
from mcp_rag_agent.core.log_setup import mask_sensitive

logger = logging.getLogger("Checkpointer")


def get_checkpointer(
    cfg: Optional[Config] = None, fallback_on_error: bool = True
) -> Optional[BaseCheckpointSaver]:
    """Factory to construct a conversation checkpointer according to configuration.

    - If FEATURE_FLAG_SESSION_MEMORY_ENABLED=false: returns None (stateless).
    - If configured for local storage (default): initializes and returns a persistent SqliteSaver.
    - If configured with a MongoDB URI: connects to MongoDB Atlas and returns a MongoDBSaver.
    - If database connection or initialization fails: catches the exception, logs a warning
      (scrubbing sensitive info), and gracefully degrades to MemorySaver (or None).

    Args:
        cfg: Optional Config instance override.
        fallback_on_error: Whether to fall back to MemorySaver on database errors.

    Returns:
        BaseCheckpointSaver or None if session memory is disabled.
    """
    active_cfg = cfg or config

    # 1. Feature Flag Check
    if not active_cfg.ff_session_memory:
        logger.info(
            "[CHECKPOINTER] Session memory is disabled via FEATURE_FLAG_SESSION_MEMORY_ENABLED=false."
        )
        return None

    # 2. Database URL & Name Validation
    if not active_cfg.db_url or not active_cfg.db_name:
        logger.warning(
            "[CHECKPOINTER] Missing db_url or db_name in configuration. "
            "Gracefully degrading to in-memory checkpointer."
        )
        return MemorySaver() if fallback_on_error else None

    # 3. Check if MongoDB URI is explicitly requested
    is_mongodb = (
        active_cfg.db_url.startswith("mongodb://")
        or active_cfg.db_url.startswith("mongodb+srv://")
    )

    if is_mongodb:
        try:
            safe_url = mask_sensitive(active_cfg.db_url)
            logger.debug(
                f"[CHECKPOINTER] Connecting to MongoDB for session checkpoints: {safe_url}"
            )

            if MongoClient is None or MongoDBSaver is None:
                raise RuntimeError("pymongo and langgraph-checkpoint-mongodb are not installed")

            client = MongoClient(
                active_cfg.db_url,
                serverSelectionTimeoutMS=2000,
                connectTimeoutMS=2000,
            )

            # Health ping to ensure server is reachable before initializing saver indexes
            client.admin.command("ping")

            checkpointer = MongoDBSaver(
                client=client,
                db_name=active_cfg.db_name,
                checkpoint_collection_name=active_cfg.db_checkpoints_collection,
                writes_collection_name=active_cfg.db_checkpoint_writes_collection,
                ttl=active_cfg.session_memory_ttl_seconds,
            )

            logger.info(
                f"[CHECKPOINTER] Initialized MongoDBSaver on database '{active_cfg.db_name}' "
                f"collection '{active_cfg.db_checkpoints_collection}'."
            )
            return checkpointer

        except Exception as exc:
            safe_err = mask_sensitive(str(exc))
            logger.warning(
                f"[CHECKPOINTER] MongoDB connection failed: {safe_err}. "
                "Gracefully degrading to in-memory checkpointer (MemorySaver)."
            )
            if fallback_on_error:
                return MemorySaver()
            return None

    # 4. Local SQLite Checkpointer Initialization
    try:
        db_path = getattr(active_cfg, "local_db_path", "./data/local_storage.db")
        if active_cfg.db_url and not active_cfg.db_url.startswith("sqlite://") and not is_mongodb:
            db_path = active_cfg.db_url
        elif db_path.startswith("sqlite:///"):
            db_path = db_path.replace("sqlite:///", "")

        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        safe_path = mask_sensitive(db_path)
        logger.debug(f"[CHECKPOINTER] Connecting to local SQLite for session checkpoints: {safe_path}")

        if SqliteSaver is None:
            raise RuntimeError("langgraph-checkpoint-sqlite is not installed")

        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA busy_timeout=5000;")

        saver_cls = CompatibleSqliteSaver or SqliteSaver
        checkpointer = saver_cls(conn)
        checkpointer.setup()

        logger.info(f"[CHECKPOINTER] Initialized local SqliteSaver at '{db_path}'.")
        return checkpointer

    except Exception as exc:
        safe_err = mask_sensitive(str(exc))
        logger.warning(
            f"[CHECKPOINTER] Local database connection failed: {safe_err}. "
            "Gracefully degrading to in-memory checkpointer (MemorySaver)."
        )
        if fallback_on_error:
            return MemorySaver()
        return None


async def get_checkpointer_async(
    cfg: Optional[Config] = None, fallback_on_error: bool = True
) -> Optional[BaseCheckpointSaver]:
    """Asynchronous wrapper to initialize checkpointer off the event loop thread."""
    return await asyncio.to_thread(get_checkpointer, cfg, fallback_on_error)

