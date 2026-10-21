"""MongoDB persistence adapter for devices with in-memory fallback support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from mcp_rag_agent.it_support.devices.models import DeviceRecord
from mcp_rag_agent.mongodb import MongoDBClient


class DeviceNotFoundError(KeyError):
    """Raised when a requested device cannot be found."""

    pass


def _get_default_seed_devices() -> dict[str, DeviceRecord]:
    now = datetime.now(timezone.utc)
    seed = [
        DeviceRecord(
            device_id="DEV-001",
            user_id="EMP-1001",
            device_type="laptop",
            manufacturer="Apple",
            model='MacBook Pro 16" M3',
            os="macOS",
            os_version="14.3.1",
            hostname="MAC-JDOE-01",
            status="active",
            vpn_client_version="5.1.2",
            security_status="compliant",
            created_at=now,
            updated_at=now,
        ),
        DeviceRecord(
            device_id="DEV-002",
            user_id="EMP-1002",
            device_type="laptop",
            manufacturer="Dell",
            model="XPS 15 9530",
            os="Windows",
            os_version="11 Pro 23H2",
            hostname="WIN-JSMITH-01",
            status="active",
            vpn_client_version="5.0.8",
            security_status="compliant",
            created_at=now,
            updated_at=now,
        ),
        DeviceRecord(
            device_id="DEV-003",
            user_id="EMP-1003",
            device_type="laptop",
            manufacturer="Lenovo",
            model="ThinkPad X1 Carbon Gen 11",
            os="Windows",
            os_version="11 Enterprise",
            hostname="WIN-AJOHN-01",
            status="active",
            vpn_client_version="5.1.0",
            security_status="compliant",
            created_at=now,
            updated_at=now,
        ),
        DeviceRecord(
            device_id="DEV-004",
            user_id="user_emp_demo",
            device_type="workstation",
            manufacturer="Dell",
            model="Precision 3660",
            os="Windows",
            os_version="11 Pro",
            hostname="WIN-DEMO-01",
            status="active",
            vpn_client_version="5.1.2",
            security_status="compliant",
            created_at=now,
            updated_at=now,
        ),
    ]
    return {d.device_id: d for d in seed}


class DeviceStore:
    """Persistence store for enterprise devices with in-memory fallback."""

    def __init__(
        self,
        mongo_client: Optional[MongoDBClient] = None,
        collection_name: str = "it_devices",
    ) -> None:
        self._mongo_client = mongo_client
        self._collection_name = collection_name
        self._in_memory_records: dict[str, DeviceRecord] = _get_default_seed_devices()

    @property
    def _collection(self) -> Any:
        if self._mongo_client is not None and getattr(self._mongo_client, "_uri", None):
            try:
                return self._mongo_client.get_collection(self._collection_name)
            except Exception:
                return None
        return None

    @staticmethod
    def _to_record(document: dict[str, Any] | None) -> DeviceRecord:
        if document is None:
            raise DeviceNotFoundError("Device not found")
        document.pop("_id", None)
        return DeviceRecord.model_validate(document)

    def create(self, device: DeviceRecord) -> DeviceRecord:
        if self._collection is not None:
            self._collection.insert_one(device.model_dump(mode="json"))
        else:
            self._in_memory_records[device.device_id] = device
        return device

    def upsert(self, device: DeviceRecord) -> DeviceRecord:
        if self._collection is not None:
            payload = device.model_dump(mode="json")
            self._collection.update_one(
                {"device_id": device.device_id},
                {"$set": payload},
                upsert=True,
            )
        else:
            self._in_memory_records[device.device_id] = device
        return device

    def get(self, device_id: str) -> DeviceRecord:
        if self._collection is not None:
            doc = self._collection.find_one({"device_id": device_id})
            return self._to_record(doc)
        if device_id not in self._in_memory_records:
            raise DeviceNotFoundError(f"Device '{device_id}' not found")
        return self._in_memory_records[device_id]

    def get_by_user(self, user_id: str) -> list[DeviceRecord]:
        if self._collection is not None:
            docs = self._collection.find({"user_id": user_id})
            return [self._to_record(doc) for doc in docs]
        return [d for d in self._in_memory_records.values() if d.user_id == user_id]

    def list(
        self, filters: dict[str, Any] | None = None, limit: int = 100
    ) -> list[DeviceRecord]:
        if self._collection is not None:
            return [
                self._to_record(item)
                for item in self._collection.find(filters or {}).limit(limit)
            ]
        results = list(self._in_memory_records.values())
        if filters:
            for k, v in filters.items():
                results = [r for r in results if getattr(r, k, None) == v]
        return results[:limit]

    def update_fields(self, device_id: str, fields: dict[str, Any]) -> DeviceRecord:
        payload = {**fields, "updated_at": datetime.now(timezone.utc).isoformat()}
        if self._collection is not None:
            result = self._collection.update_one(
                {"device_id": device_id}, {"$set": payload}
            )
            if not result.matched_count:
                raise DeviceNotFoundError(f"Device '{device_id}' not found")
            return self.get(device_id)

        if device_id not in self._in_memory_records:
            raise DeviceNotFoundError(f"Device '{device_id}' not found")
        data = self._in_memory_records[device_id].model_dump()
        data.update(payload)
        self._in_memory_records[device_id] = DeviceRecord.model_validate(data)
        return self._in_memory_records[device_id]

