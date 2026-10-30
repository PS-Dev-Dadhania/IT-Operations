"""Local database package for persistent SQLite, FTS5, and vector storage."""

from mcp_rag_agent.database.client import (
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    LocalCollection,
    LocalCursor,
    LocalDatabaseClient,
    UpdateResult,
)

__all__ = [
    "LocalDatabaseClient",
    "LocalCollection",
    "LocalCursor",
    "InsertOneResult",
    "InsertManyResult",
    "UpdateResult",
    "DeleteResult",
]
