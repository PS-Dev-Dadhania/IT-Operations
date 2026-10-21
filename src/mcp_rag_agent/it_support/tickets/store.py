"""MongoDB persistence adapter for tickets with in-memory fallback support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from mcp_rag_agent.it_support.models import ITCategory, Priority
from mcp_rag_agent.it_support.tickets.models import (
    TicketComment,
    TicketLifecycleStatus,
    TicketRecord,
)
from mcp_rag_agent.mongodb import MongoDBClient


class TicketNotFoundError(KeyError):
    pass


def _get_default_seed_tickets() -> dict[str, TicketRecord]:
    now = datetime.now(timezone.utc)
    seed = [
        TicketRecord(
            ticket_id="TKT-1001",
            title="Cannot connect to Corporate VPN (US-East Gateway)",
            description="VPN client fails with handshake timeout on gateway vpn-east.corp.internal after macOS upgrade.",
            category=ITCategory.VPN,
            priority=Priority.HIGH,
            status=TicketLifecycleStatus.OPEN,
            requester_id="EMP-1001",
            assigned_team="Network Support",
            created_at=now,
            updated_at=now,
        ),
        TicketRecord(
            ticket_id="TKT-1002",
            title="Okta Authenticator MFA Token Push Delay",
            description="Push notifications arrive after 3-minute delay or fail with invalid session code.",
            category=ITCategory.ACCESS,
            priority=Priority.MEDIUM,
            status=TicketLifecycleStatus.IN_PROGRESS,
            requester_id="EMP-1002",
            assigned_team="Tier 1 Support",
            created_at=now,
            updated_at=now,
        ),
        TicketRecord(
            ticket_id="TKT-1003",
            title="CorpNet-Secure Wi-Fi 802.1X Certificate Expired",
            description="Device unable to authenticate to 802.1X EAP-TLS corporate wireless profile.",
            category=ITCategory.NETWORK,
            priority=Priority.LOW,
            status=TicketLifecycleStatus.RESOLVED,
            requester_id="EMP-1003",
            assigned_team="Desktop Support",
            created_at=now,
            updated_at=now,
        ),
        TicketRecord(
            ticket_id="TKT-1004",
            title="Suspicious Executive Impersonation Phishing Email",
            description="User reported spear-phishing wire transfer attempt pretending to be CFO.",
            category=ITCategory.SECURITY,
            priority=Priority.CRITICAL,
            status=TicketLifecycleStatus.ESCALATED,
            requester_id="EMP-1001",
            assigned_team="Security Operations",
            created_at=now,
            updated_at=now,
        ),
    ]
    return {t.ticket_id: t for t in seed}


class TicketStore:
    def __init__(
        self,
        mongo_client: Optional[MongoDBClient] = None,
        collection_name: str = "it_tickets",
    ) -> None:
        self._mongo_client = mongo_client
        self._collection_name = collection_name
        self._in_memory_records: dict[str, TicketRecord] = _get_default_seed_tickets()

    @property
    def _collection(self) -> Any:
        if self._mongo_client is not None and getattr(self._mongo_client, "_uri", None):
            try:
                return self._mongo_client.get_collection(self._collection_name)
            except Exception:
                return None
        return None

    @staticmethod
    def _to_record(document: dict[str, Any] | None) -> TicketRecord:
        if document is None:
            raise TicketNotFoundError("Ticket not found")
        document.pop("_id", None)
        return TicketRecord.model_validate(document)

    def create(self, ticket: TicketRecord) -> TicketRecord:
        if self._collection is not None:
            self._collection.insert_one(ticket.model_dump(mode="json"))
        else:
            self._in_memory_records[ticket.ticket_id] = ticket
        return ticket

    def get(self, ticket_id: str) -> TicketRecord:
        if self._collection is not None:
            return self._to_record(self._collection.find_one({"ticket_id": ticket_id}))
        if ticket_id not in self._in_memory_records:
            raise TicketNotFoundError(ticket_id)
        return self._in_memory_records[ticket_id]

    def list(
        self, filters: dict[str, Any] | None = None, limit: int = 100
    ) -> list[TicketRecord]:
        if self._collection is not None:
            return [
                self._to_record(item)
                for item in self._collection.find(filters or {}).limit(limit)
            ]
        results = list(self._in_memory_records.values())
        if filters:
            if "status" in filters:
                st = filters["status"].lower()
                results = [
                    r for r in results
                    if (r.status.value if hasattr(r.status, "value") else str(r.status)).lower() == st
                ]
            if "priority" in filters:
                pr = filters["priority"].lower()
                results = [
                    r for r in results
                    if (r.priority.value if hasattr(r.priority, "value") else str(r.priority)).lower() == pr
                ]
            if "category" in filters:
                cat = filters["category"].lower()
                results = [
                    r for r in results
                    if (r.category.value if hasattr(r.category, "value") else str(r.category)).lower() == cat
                ]
            if "requester_id" in filters:
                results = [r for r in results if r.requester_id == filters["requester_id"]]
        return results[:limit]

    def list_tickets(
        self, filters: dict[str, Any] | None = None, limit: int = 100
    ) -> list[TicketRecord]:
        return self.list(filters, limit)

    def find_unresolved_duplicate(self, ticket: TicketRecord) -> TicketRecord | None:
        if self._collection is not None:
            query: dict[str, Any] = {
                "requester_id": ticket.requester_id,
                "status": {
                    "$in": [
                        TicketLifecycleStatus.NEW.value,
                        TicketLifecycleStatus.OPEN.value,
                        TicketLifecycleStatus.IN_PROGRESS.value,
                        TicketLifecycleStatus.WAITING_FOR_USER.value,
                        TicketLifecycleStatus.ESCALATED.value,
                    ]
                },
                "category": ticket.category.value,
                "title": ticket.title,
            }
            for key in ("product", "platform", "error_code"):
                value = getattr(ticket, key)
                if value:
                    query[key] = value
            found = self._collection.find_one(query)
            return self._to_record(found) if found else None

        active_statuses = {
            TicketLifecycleStatus.NEW.value,
            TicketLifecycleStatus.OPEN.value,
            TicketLifecycleStatus.IN_PROGRESS.value,
            TicketLifecycleStatus.WAITING_FOR_USER.value,
            TicketLifecycleStatus.ESCALATED.value,
        }
        for r in self._in_memory_records.values():
            st = r.status.value if hasattr(r.status, "value") else str(r.status)
            if (
                r.requester_id == ticket.requester_id
                and st in active_statuses
                and r.title == ticket.title
            ):
                return r
        return None

    def update_fields(self, ticket_id: str, fields: dict[str, Any]) -> TicketRecord:
        payload = {**fields, "updated_at": datetime.now(timezone.utc).isoformat()}
        if self._collection is not None:
            result = self._collection.update_one(
                {"ticket_id": ticket_id}, {"$set": payload}
            )
            if not result.matched_count:
                raise TicketNotFoundError(ticket_id)
            return self.get(ticket_id)

        if ticket_id not in self._in_memory_records:
            raise TicketNotFoundError(ticket_id)
        current = self._in_memory_records[ticket_id].model_dump()
        current.update(payload)
        self._in_memory_records[ticket_id] = TicketRecord.model_validate(current)
        return self._in_memory_records[ticket_id]

    def update(self, ticket_id: str, fields: dict[str, Any]) -> TicketRecord:
        return self.update_fields(ticket_id, fields)

    def update_status(
        self, ticket_id: str, status: TicketLifecycleStatus
    ) -> TicketRecord:
        return self.update_fields(ticket_id, {"status": status.value})

    def assign_team(self, ticket_id: str, team: str | None) -> TicketRecord:
        return self.update_fields(ticket_id, {"assigned_team": team})

    def add_comment(self, ticket_id: str, comment: TicketComment) -> TicketRecord:
        if self._collection is not None:
            result = self._collection.update_one(
                {"ticket_id": ticket_id},
                {
                    "$push": {"comments": comment.model_dump(mode="json")},
                    "$set": {"updated_at": datetime.now(timezone.utc).isoformat()},
                },
            )
            if not result.matched_count:
                raise TicketNotFoundError(ticket_id)
            return self.get(ticket_id)

        rec = self.get(ticket_id)
        updated_comments = list(rec.comments) + [comment]
        return self.update_fields(ticket_id, {"comments": [c.model_dump(mode="json") for c in updated_comments]})

