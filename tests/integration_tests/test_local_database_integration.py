"""Integration tests for live Local SQLite Database, Hybrid Search, and LangGraph Checkpoints."""

import os
import shutil
import tempfile
import uuid
from datetime import datetime, timezone

import pytest
from langgraph.checkpoint.sqlite import SqliteSaver

from mcp_rag_agent.database.client import LocalDatabaseClient
from mcp_rag_agent.it_support.tickets.models import (
    TicketComment,
    TicketRecord,
    ITCategory,
    Priority,
    TicketLifecycleStatus,
)
from mcp_rag_agent.it_support.tickets.store import TicketStore
from mcp_rag_agent.it_support.incidents.models import IncidentRecord, IncidentStatus
from mcp_rag_agent.it_support.incidents.store import IncidentStore
from mcp_rag_agent.it_support.users.models import UserContextRecord, SupportTier, UserStatus
from mcp_rag_agent.it_support.users.store import UserStore


@pytest.fixture
def test_db_env():
    """Create a temporary local SQLite database environment."""
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, "integration_test.db")
    client = LocalDatabaseClient(database_path=db_path)
    client.connect()
    yield client, db_path
    client.disconnect()
    shutil.rmtree(temp_dir, ignore_errors=True)


class TestLocalDatabaseIntegration:
    """Live integration test suite verifying end-to-end functionality of the local storage layer."""

    def test_live_local_ping_and_tables(self, test_db_env):
        """Verify client connects and responds to ping."""
        client, db_path = test_db_env
        assert client.ping() is True
        assert os.path.exists(db_path)

    def test_live_document_crud_and_persistence(self, test_db_env):
        """Verify CRUD operations against local SQLite database."""
        client, db_path = test_db_env
        col = client.get_collection("test_integration_docs")

        doc_id = str(uuid.uuid4())
        test_doc = {
            "_id": doc_id,
            "title": "Local Storage Integration Test",
            "category": "infrastructure",
            "metadata": {"env": "local", "tier": "gold"},
        }

        # 1. Insert
        res = col.insert_one(test_doc)
        assert res.inserted_id == doc_id

        # 2. Read
        found = col.find_one({"_id": doc_id})
        assert found is not None
        assert found["title"] == "Local Storage Integration Test"
        assert found["metadata"]["env"] == "local"

        # 3. Update
        update_res = col.update_one(
            {"_id": doc_id},
            {"$set": {"status": "verified", "metadata.tier": "platinum"}},
        )
        assert update_res.matched_count == 1
        updated = col.find_one({"_id": doc_id})
        assert updated["status"] == "verified"
        assert updated["metadata"]["tier"] == "platinum"

        # 4. Verify persistence across client reopen
        client.disconnect()
        new_client = LocalDatabaseClient(database_path=db_path)
        new_client.connect()
        try:
            persisted = new_client.get_collection("test_integration_docs").find_one({"_id": doc_id})
            assert persisted is not None
            assert persisted["status"] == "verified"
        finally:
            new_client.disconnect()

    def test_live_hybrid_retrieval_and_ranking(self, test_db_env):
        """Verify vector cosine search, FTS5 lexical search, and RRF fusion."""
        client, _ = test_db_env

        # Seed KB articles with 256-dimensional embeddings
        v_vpn = [0.0] * 256
        v_vpn[0] = 0.95
        v_vpn[1] = 0.25

        v_okta = [0.0] * 256
        v_okta[2] = 0.90
        v_okta[3] = 0.30

        v_wifi = [0.0] * 256
        v_wifi[4] = 0.85
        v_wifi[5] = 0.40

        client.insert_documents("kb_vectors", [
            {
                "chunk_id": "chunk_vpn_01",
                "content": "GlobalProtect VPN Gateway Troubleshooting and macOS Certificate Configuration",
                "embedding": v_vpn,
                "metadata": {"doc_id": "vpn_doc", "category": "vpn"},
            },
            {
                "chunk_id": "chunk_okta_01",
                "content": "Okta Verify Push Notification Delays and MFA Token Reset Procedures",
                "embedding": v_okta,
                "metadata": {"doc_id": "okta_doc", "category": "access"},
            },
            {
                "chunk_id": "chunk_wifi_01",
                "content": "Corporate 802.1X Wireless Network Authentication and EAP-TLS Profile",
                "embedding": v_wifi,
                "metadata": {"doc_id": "wifi_doc", "category": "network"},
            },
        ])

        # Query vector aligned with VPN
        q_vec = [0.0] * 256
        q_vec[0] = 0.90
        q_vec[1] = 0.20

        # Hybrid Search: VPN query
        results = client.hybrid_search(
            collection_name="kb_vectors",
            query_vector=q_vec,
            query_text="VPN certificate configuration troubleshooting",
            limit=2,
            semantic_weight=0.7,
        )

        assert len(results) >= 1
        top_match = results[0]
        assert "VPN" in top_match["content"]
        assert "rrf_score" in top_match
        assert top_match["rrf_score"] > 0
        assert top_match["chunk_id"] == "chunk_vpn_01"

    def test_live_it_support_stores_integration(self, test_db_env):
        """Verify IT Support stores (TicketStore, UserStore, IncidentStore) persist and query."""
        client, db_path = test_db_env
        now = datetime.now(timezone.utc)

        # 1. User Store
        user_store = UserStore(client)
        user = UserContextRecord(
            user_id="EMP-TEST-01",
            name="Test Engineer",
            email="test.eng@corp.local",
            department="DevOps",
            role="Site Reliability Engineer",
            support_tier=SupportTier.TIER_2,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now,
        )
        user_store.create(user)
        fetched_user = user_store.get("EMP-TEST-01")
        assert fetched_user.name == "Test Engineer"
        assert fetched_user.department == "DevOps"

        # 2. Ticket Store with comments
        ticket_store = TicketStore(client)
        ticket = TicketRecord(
            ticket_id="TKT-LIVE-01",
            title="Database Latency Spike in Production",
            description="P99 latency exceeded 200ms on primary cluster.",
            category=ITCategory.HARDWARE,
            priority=Priority.CRITICAL,
            status=TicketLifecycleStatus.OPEN,
            requester_id="EMP-TEST-01",
            assigned_team="Database Ops",
            created_at=now,
            updated_at=now,
        )
        ticket_store.create(ticket)

        comment = TicketComment(author_id="EMP-TEST-01", body="Investigating index usage.")
        ticket_store.add_comment("TKT-LIVE-01", comment)
        ticket_store.update_status("TKT-LIVE-01", TicketLifecycleStatus.IN_PROGRESS)

        updated_ticket = ticket_store.get("TKT-LIVE-01")
        assert updated_ticket.status == TicketLifecycleStatus.IN_PROGRESS
        assert len(updated_ticket.comments) == 1
        assert updated_ticket.comments[0].body == "Investigating index usage."

        # 3. Incident Store
        incident_store = IncidentStore(client)
        incident = IncidentRecord(
            incident_id="INC-LIVE-01",
            title="Okta Authentication Service Degradation",
            description="Push notifications experiencing elevated latency.",
            service="okta",
            status=IncidentStatus.INVESTIGATING,
            severity=Priority.HIGH,
            start_time=now,
            created_at=now,
            updated_at=now,
        )
        incident_store.create(incident)
        active_incidents = incident_store.list_active()
        assert any(inc.incident_id == "INC-LIVE-01" for inc in active_incidents)

        # 4. Verify all persisted after reopening database
        client.disconnect()
        reopen_client = LocalDatabaseClient(database_path=db_path)
        reopen_client.connect()
        try:
            reopen_t_store = TicketStore(reopen_client)
            persisted_tkt = reopen_t_store.get("TKT-LIVE-01")
            assert persisted_tkt.status == TicketLifecycleStatus.IN_PROGRESS
            assert len(persisted_tkt.comments) == 1
        finally:
            reopen_client.disconnect()

    def test_live_langgraph_checkpoint_persistence(self, test_db_env):
        """Verify LangGraph SqliteSaver persists state and thread checkpoints across connection close."""
        import sqlite3
        _, db_path = test_db_env

        # 1. Connect and save checkpoint on thread_100
        conn1 = sqlite3.connect(db_path, check_same_thread=False)
        saver1 = SqliteSaver(conn1)
        saver1.setup()

        thread_config = {"configurable": {"thread_id": "thread_100", "checkpoint_ns": ""}}
        checkpoint_data = {
            "v": 1,
            "id": "chk_001",
            "ts": "2026-10-23T12:00:00Z",
            "channel_values": {"messages": ["Hello, how can I configure VPN?"]},
            "channel_versions": {"messages": 1},
            "versions_seen": {},
        }
        metadata = {"source": "input", "step": 1, "writes": {}}

        saver1.put(thread_config, checkpoint_data, metadata, {})
        conn1.close()

        # 2. Reopen connection from scratch on same file and verify checkpoint
        conn2 = sqlite3.connect(db_path, check_same_thread=False)
        saver2 = SqliteSaver(conn2)
        tuple_res = saver2.get_tuple(thread_config)

        assert tuple_res is not None
        assert tuple_res.checkpoint["id"] == "chk_001"
        assert tuple_res.checkpoint["channel_values"]["messages"] == ["Hello, how can I configure VPN?"]
        conn2.close()
