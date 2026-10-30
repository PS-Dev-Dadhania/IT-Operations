"""Backward compatibility wrapper mapping MongoDBClient to LocalDatabaseClient."""

from mcp_rag_agent.database.client import LocalDatabaseClient
from mcp_rag_agent.mongodb.client import MongoDBClient

__all__ = ["MongoDBClient", "LocalDatabaseClient"]
