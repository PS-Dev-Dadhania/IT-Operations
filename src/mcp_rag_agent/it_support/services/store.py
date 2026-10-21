"""MongoDB persistence adapter for service statuses with in-memory fallback support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from mcp_rag_agent.it_support.services.models import (
    ServiceOperationalStatus,
    ServiceStatusRecord,
)
from mcp_rag_agent.mongodb import MongoDBClient


class ServiceNotFoundError(KeyError):
    """Raised when a requested service status cannot be found."""

    pass


def _get_default_seed_services() -> dict[str, ServiceStatusRecord]:
    now = datetime.now(timezone.utc)
    seed = [
        ServiceStatusRecord(
            service_name="corporate_vpn",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="Corporate VPN Gateways (US-East, US-West, EU-Central) operational.",
        ),
        ServiceStatusRecord(
            service_name="corporate_wifi",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="Enterprise 802.1X wireless controllers operational.",
        ),
        ServiceStatusRecord(
            service_name="github",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="GitHub Enterprise Cloud SSO & Repo Access operational.",
        ),
        ServiceStatusRecord(
            service_name="jira",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="Atlassian Cloud Jira Software & Service Desk operational.",
        ),
        ServiceStatusRecord(
            service_name="outlook",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="Microsoft 365 Exchange Online and Outlook Web Access operational.",
        ),
        ServiceStatusRecord(
            service_name="teams",
            status=ServiceOperationalStatus.OPERATIONAL,
            last_updated=now,
            message="Microsoft Teams chat, meetings, and calling services operational.",
        ),
    ]
    return {s.service_name: s for s in seed}


class ServiceStatusStore:
    """Persistence store for enterprise service statuses with in-memory fallback."""

    def __init__(
        self,
        mongo_client: Optional[MongoDBClient] = None,
        collection_name: str = "it_service_statuses",
    ) -> None:
        self._mongo_client = mongo_client
        self._collection_name = collection_name
        self._in_memory_records: dict[str, ServiceStatusRecord] = _get_default_seed_services()

    @property
    def _collection(self) -> Any:
        if self._mongo_client is not None and getattr(self._mongo_client, "_uri", None):
            try:
                return self._mongo_client.get_collection(self._collection_name)
            except Exception:
                return None
        return None

    @staticmethod
    def _to_record(document: dict[str, Any] | None) -> ServiceStatusRecord:
        if document is None:
            raise ServiceNotFoundError("Service status not found")
        document.pop("_id", None)
        return ServiceStatusRecord.model_validate(document)

    def upsert(self, record: ServiceStatusRecord) -> ServiceStatusRecord:
        if self._collection is not None:
            payload = record.model_dump(mode="json")
            self._collection.update_one(
                {"service_name": record.service_name},
                {"$set": payload},
                upsert=True,
            )
        else:
            self._in_memory_records[record.service_name] = record
        return record

    def get(self, service_name: str) -> ServiceStatusRecord:
        if self._collection is not None:
            doc = self._collection.find_one({"service_name": service_name})
            return self._to_record(doc)
        if service_name not in self._in_memory_records:
            raise ServiceNotFoundError(f"Service status '{service_name}' not found")
        return self._in_memory_records[service_name]

    def list_all(self) -> list[ServiceStatusRecord]:
        if self._collection is not None:
            return [self._to_record(item) for item in self._collection.find({})]
        return list(self._in_memory_records.values())

