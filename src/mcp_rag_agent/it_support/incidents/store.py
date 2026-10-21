"""MongoDB persistence adapter for incidents with in-memory fallback support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from mcp_rag_agent.it_support.incidents.models import (
    IncidentMatchCriteria,
    IncidentRecord,
)
from mcp_rag_agent.it_support.models import IncidentStatus, Priority
from mcp_rag_agent.mongodb import MongoDBClient


class IncidentNotFoundError(KeyError):
    pass


def _get_default_seed_incidents() -> dict[str, IncidentRecord]:
    now = datetime.now(timezone.utc)
    seed = [
        IncidentRecord(
            incident_id="INC-2001",
            title="Global VPN Gateway High Packet Loss",
            description="High latency and packet loss impacting North America and Europe VPN ingress gateways.",
            service="vpn",
            severity=Priority.CRITICAL,
            status=IncidentStatus.INVESTIGATING,
            affected_users=185,
            workaround="Route traffic through secondary gateway (vpn-backup.corp.xyz).",
            created_at=now,
            updated_at=now,
        ),
        IncidentRecord(
            incident_id="INC-2002",
            title="GitHub Enterprise Cloud Webhooks Delay",
            description="Upstream delay in CI/CD pipeline triggers and webhook deliveries.",
            service="github",
            severity=Priority.MEDIUM,
            status=IncidentStatus.MONITORING,
            affected_users=45,
            workaround="Trigger GitHub Actions workflows manually if delayed > 5 minutes.",
            created_at=now,
            updated_at=now,
        ),
        IncidentRecord(
            incident_id="INC-2003",
            title="Microsoft Outlook Web Access Intermittent 503 Errors",
            description="Exchange Online authentication timeout intermittently affecting web sessions.",
            service="outlook",
            severity=Priority.HIGH,
            status=IncidentStatus.RESOLVED,
            affected_users=320,
            workaround="Use Outlook Desktop or Mobile app while web services recover.",
            created_at=now,
            updated_at=now,
        ),
    ]
    return {i.incident_id: i for i in seed}


class IncidentStore:
    def __init__(
        self,
        mongo_client: Optional[MongoDBClient] = None,
        collection_name: str = "it_incidents",
    ) -> None:
        self._mongo_client = mongo_client
        self._collection_name = collection_name
        self._in_memory_records: dict[str, IncidentRecord] = _get_default_seed_incidents()

    @property
    def _collection(self) -> Any:
        if self._mongo_client is not None and getattr(self._mongo_client, "_uri", None):
            try:
                return self._mongo_client.get_collection(self._collection_name)
            except Exception:
                return None
        return None

    @staticmethod
    def _to_record(document: dict[str, Any] | None) -> IncidentRecord:
        if document is None:
            raise IncidentNotFoundError("Incident not found")
        document.pop("_id", None)
        return IncidentRecord.model_validate(document)

    def create(self, incident: IncidentRecord) -> IncidentRecord:
        if self._collection is not None:
            self._collection.insert_one(incident.model_dump(mode="json"))
        else:
            self._in_memory_records[incident.incident_id] = incident
        return incident

    def get(self, incident_id: str) -> IncidentRecord:
        if self._collection is not None:
            return self._to_record(self._collection.find_one({"incident_id": incident_id}))
        if incident_id not in self._in_memory_records:
            raise IncidentNotFoundError(incident_id)
        return self._in_memory_records[incident_id]

    def update_status(self, incident_id: str, status: IncidentStatus) -> IncidentRecord:
        updates: dict[str, Any] = {
            "status": status.value,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        if status is IncidentStatus.RESOLVED:
            updates["end_time"] = datetime.now(timezone.utc).isoformat()

        if self._collection is not None:
            result = self._collection.update_one(
                {"incident_id": incident_id}, {"$set": updates}
            )
            if not result.matched_count:
                raise IncidentNotFoundError(incident_id)
            return self.get(incident_id)

        if incident_id not in self._in_memory_records:
            raise IncidentNotFoundError(incident_id)
        data = self._in_memory_records[incident_id].model_dump()
        data.update(updates)
        self._in_memory_records[incident_id] = IncidentRecord.model_validate(data)
        return self._in_memory_records[incident_id]

    def list_active(self, limit: int = 100) -> list[IncidentRecord]:
        statuses = [
            IncidentStatus.INVESTIGATING.value,
            IncidentStatus.IDENTIFIED.value,
            IncidentStatus.MONITORING.value,
        ]
        if self._collection is not None:
            return [
                self._to_record(item)
                for item in self._collection.find({"status": {"$in": statuses}}).limit(
                    limit
                )
            ]
        return [
            r for r in self._in_memory_records.values()
            if (r.status.value if hasattr(r.status, "value") else str(r.status)).lower() in statuses
        ][:limit]

    def list_all(self, limit: int = 100) -> list[IncidentRecord]:
        if self._collection is not None:
            return [
                self._to_record(item) for item in self._collection.find({}).limit(limit)
            ]
        return list(self._in_memory_records.values())[:limit]

    def find_matching(self, criteria: IncidentMatchCriteria) -> list[IncidentRecord]:
        """Return active exact structured candidates for deterministic scoring."""
        if self._collection is not None:
            query: dict[str, Any] = {
                "service": criteria.service,
                "status": {
                    "$in": [
                        IncidentStatus.INVESTIGATING.value,
                        IncidentStatus.IDENTIFIED.value,
                        IncidentStatus.MONITORING.value,
                    ]
                },
            }
            for name in ("product", "platform", "category", "error_code"):
                value = getattr(criteria, name)
                if value is not None:
                    query[name] = value.value if hasattr(value, "value") else value
            return [
                self._to_record(item) for item in self._collection.find(query).limit(100)
            ]

        active_statuses = {"investigating", "identified", "monitoring"}
        matched = []
        for r in self._in_memory_records.values():
            st = (r.status.value if hasattr(r.status, "value") else str(r.status)).lower()
            if r.service.lower() == criteria.service.lower() and st in active_statuses:
                matched.append(r)
        return matched[:100]

