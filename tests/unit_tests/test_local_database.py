"""Comprehensive unit tests for the LocalDatabaseClient and SQLite storage layer."""

import os
import shutil
import tempfile
import pytest

from mcp_rag_agent.database.client import LocalDatabaseClient


@pytest.fixture
def temp_db():
    """Create a temporary directory and database path for test isolation."""
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, "test_local.db")
    client = LocalDatabaseClient(database_path=db_path)
    client.connect()
    yield client, db_path
    client.disconnect()
    shutil.rmtree(temp_dir, ignore_errors=True)


class TestLocalDatabaseClient:
    """Test suite for LocalDatabaseClient operations."""

    def test_client_connect_and_ping(self, temp_db):
        client, db_path = temp_db
        assert client.ping() is True
        assert os.path.exists(db_path)

    def test_collection_lifecycle(self, temp_db):
        client, _ = temp_db
        assert not client.collection_exists("test_col")
        client.create_collection("test_col")
        assert client.collection_exists("test_col")
        assert "test_col" in client.list_collections()

    def test_document_insert_and_find(self, temp_db):
        client, _ = temp_db
        col = client.get_collection("users")

        doc_id = client.insert_document("users", {
            "user_id": "EMP-001",
            "name": "Alice Smith",
            "department": "Engineering",
            "tier": 2,
            "metadata": {"location": "NYC", "project": "Copilot"},
        })
        assert doc_id is not None

        # find_one by exact field
        found = col.find_one({"user_id": "EMP-001"})
        assert found is not None
        assert found["name"] == "Alice Smith"
        assert found["metadata"]["location"] == "NYC"

        # find with dot notation
        dot_found = col.find_one({"metadata.project": "Copilot"})
        assert dot_found is not None
        assert dot_found["user_id"] == "EMP-001"

    def test_query_operators(self, temp_db):
        client, _ = temp_db
        col = client.get_collection("items")

        client.insert_documents("items", [
            {"sku": "A", "price": 10, "status": "active"},
            {"sku": "B", "price": 20, "status": "active"},
            {"sku": "C", "price": 30, "status": "pending"},
            {"sku": "D", "price": 40, "status": "archived"},
        ])

        # $in
        in_res = list(col.find({"status": {"$in": ["pending", "archived"]}}))
        assert len(in_res) == 2
        assert {d["sku"] for d in in_res} == {"C", "D"}

        # $gte and $lte
        range_res = list(col.find({"price": {"$gte": 15, "$lte": 35}}))
        assert len(range_res) == 2
        assert {d["sku"] for d in range_res} == {"B", "C"}

        # $ne
        ne_res = list(col.find({"status": {"$ne": "active"}}))
        assert len(ne_res) == 2

    def test_update_and_push(self, temp_db):
        client, _ = temp_db
        col = client.get_collection("tickets")

        col.insert_one({
            "ticket_id": "TKT-101",
            "status": "OPEN",
            "comments": [],
        })

        # Test $set and $push
        res = col.update_one(
            {"ticket_id": "TKT-101"},
            {
                "$set": {"status": "IN_PROGRESS"},
                "$push": {"comments": {"author": "agent", "body": "Working on it"}},
            },
        )
        assert res.matched_count == 1
        assert res.modified_count == 1

        updated = col.find_one({"ticket_id": "TKT-101"})
        assert updated["status"] == "IN_PROGRESS"
        assert len(updated["comments"]) == 1
        assert updated["comments"][0]["body"] == "Working on it"

    def test_upsert(self, temp_db):
        client, _ = temp_db
        col = client.get_collection("users")

        # Upsert a new record
        res = col.update_one(
            {"user_id": "EMP-999"},
            {"$set": {"name": "New User", "role": "Analyst"}},
            upsert=True,
        )
        assert res.matched_count == 0

        found = col.find_one({"user_id": "EMP-999"})
        assert found is not None
        assert found["name"] == "New User"

        # Upsert update existing
        res2 = col.update_one(
            {"user_id": "EMP-999"},
            {"$set": {"role": "Senior Analyst"}},
            upsert=True,
        )
        assert res2.matched_count == 1
        assert col.find_one({"user_id": "EMP-999"})["role"] == "Senior Analyst"

    def test_delete_operations(self, temp_db):
        client, _ = temp_db
        col = client.get_collection("logs")

        client.insert_documents("logs", [
            {"level": "INFO", "msg": "1"},
            {"level": "ERROR", "msg": "2"},
            {"level": "INFO", "msg": "3"},
        ])

        del_res = col.delete_many({"level": "INFO"})
        assert del_res.deleted_count == 2
        remaining = list(col.find({}))
        assert len(remaining) == 1
        assert remaining[0]["level"] == "ERROR"

    def test_vector_search(self, temp_db):
        client, _ = temp_db

        v1 = [1.0, 0.0, 0.0]
        v2 = [0.0, 1.0, 0.0]
        v3 = [0.8, 0.2, 0.0]

        client.insert_documents("vectors", [
            {"content": "apple doc", "embedding": v1, "category": "fruit"},
            {"content": "carrot doc", "embedding": v2, "category": "vegetable"},
            {"content": "orange doc", "embedding": v3, "category": "fruit"},
        ])

        # Search with query vector closest to v1
        results = client.vector_search(
            collection_name="vectors",
            query_vector=[0.9, 0.1, 0.0],
            limit=2,
            min_score=0.5,
        )
        assert len(results) == 2
        assert results[0]["content"] in ("apple doc", "orange doc")
        assert results[0]["score"] > 0.8

        # Search with filter
        filtered = client.vector_search(
            collection_name="vectors",
            query_vector=[0.9, 0.1, 0.0],
            limit=2,
            filter_query={"category": "vegetable"},
        )
        assert len(filtered) == 1
        assert filtered[0]["content"] == "carrot doc"

    def test_fts5_text_search(self, temp_db):
        client, _ = temp_db

        client.insert_documents("docs", [
            {"content": "Corporate Virtual Private Network (VPN) connection guidelines and troubleshooting"},
            {"content": "Okta multi-factor authentication push token delay and reset procedure"},
            {"content": "Hardware replacement policy for laptops and mobile devices"},
        ])

        # Keyword search for VPN
        res_vpn = client.text_search(
            collection_name="docs",
            query_text="VPN troubleshooting connection",
            limit=5,
        )
        assert len(res_vpn) >= 1
        assert "VPN" in res_vpn[0]["content"]
        assert res_vpn[0]["text_score"] > 0

    def test_hybrid_search_rrf(self, temp_db):
        client, _ = temp_db

        # Ingest docs with both text and embeddings
        client.insert_documents("kb", [
            {"content": "VPN configuration troubleshooting for remote work", "embedding": [0.9, 0.1, 0.0]},
            {"content": "Password reset and Okta MFA setup instructions", "embedding": [0.1, 0.9, 0.0]},
            {"content": "Annual leave policy and holiday calendar guidelines", "embedding": [0.0, 0.1, 0.9]},
        ])

        hybrid_results = client.hybrid_search(
            collection_name="kb",
            query_vector=[0.85, 0.15, 0.0],
            query_text="VPN remote troubleshooting",
            limit=2,
            semantic_weight=0.7,
        )

        assert len(hybrid_results) >= 1
        top = hybrid_results[0]
        assert "VPN" in top["content"]
        assert "rrf_score" in top
        assert top["rrf_score"] > 0

    def test_persistence_across_reconnect(self, temp_db):
        client, db_path = temp_db
        client.insert_document("tickets", {"ticket_id": "TKT-PERST", "status": "OPEN"})
        client.disconnect()

        # Reopen with brand new client instance pointing to same file
        reconnected_client = LocalDatabaseClient(database_path=db_path)
        reconnected_client.connect()
        try:
            col = reconnected_client.get_collection("tickets")
            doc = col.find_one({"ticket_id": "TKT-PERST"})
            assert doc is not None
            assert doc["status"] == "OPEN"
        finally:
            reconnected_client.disconnect()
