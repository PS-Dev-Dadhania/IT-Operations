"""MongoDB persistence adapter for users with in-memory fallback support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from mcp_rag_agent.it_support.users.models import (
    SupportTier,
    UserContextRecord,
    UserStatus,
)
from mcp_rag_agent.mongodb import MongoDBClient


class UserNotFoundError(KeyError):
    """Raised when a requested user cannot be found."""

    pass


def _get_default_seed_users() -> dict[str, UserContextRecord]:
    now = datetime.now(timezone.utc)
    seed = [
        UserContextRecord(
            user_id="EMP-1001",
            name="John Doe",
            email="john.doe@enterprise.internal",
            department="Engineering",
            role="Software Engineer",
            support_tier=SupportTier.STANDARD,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now,
            metadata={"location": "New York", "cost_center": "ENG-402"},
        ),
        UserContextRecord(
            user_id="EMP-1002",
            name="Jane Smith",
            email="jane.smith@enterprise.internal",
            department="Product",
            role="Product Manager",
            support_tier=SupportTier.TIER_1,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now,
            metadata={"location": "San Francisco", "cost_center": "PROD-101"},
        ),
        UserContextRecord(
            user_id="EMP-1003",
            name="Alice Johnson",
            email="alice.j@enterprise.internal",
            department="Finance",
            role="Financial Analyst",
            support_tier=SupportTier.VIP,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now,
            metadata={"location": "London", "cost_center": "FIN-203"},
        ),
        UserContextRecord(
            user_id="user_emp_demo",
            name="Alex Rivera",
            email="alex.rivera@enterprise.internal",
            department="Engineering",
            role="Support Specialist",
            support_tier=SupportTier.TIER_2,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now,
            metadata={"location": "Austin", "cost_center": "IT-001"},
        ),
    ]
    return {u.user_id: u for u in seed}


class UserStore:
    """Persistence store for enterprise user context with in-memory fallback."""

    def __init__(
        self,
        mongo_client: Optional[MongoDBClient] = None,
        collection_name: str = "it_users",
    ) -> None:
        self._mongo_client = mongo_client
        self._collection_name = collection_name
        self._in_memory_records: dict[str, UserContextRecord] = _get_default_seed_users()

    @property
    def _collection(self) -> Any:
        if self._mongo_client is not None and getattr(self._mongo_client, "_uri", None):
            try:
                return self._mongo_client.get_collection(self._collection_name)
            except Exception:
                return None
        return None

    @staticmethod
    def _to_record(document: dict[str, Any] | None) -> UserContextRecord:
        if document is None:
            raise UserNotFoundError("User not found")
        document.pop("_id", None)
        return UserContextRecord.model_validate(document)

    def create(self, user: UserContextRecord) -> UserContextRecord:
        if self._collection is not None:
            self._collection.insert_one(user.model_dump(mode="json"))
        else:
            self._in_memory_records[user.user_id] = user
        return user

    def upsert(self, user: UserContextRecord) -> UserContextRecord:
        if self._collection is not None:
            payload = user.model_dump(mode="json")
            self._collection.update_one(
                {"user_id": user.user_id},
                {"$set": payload},
                upsert=True,
            )
        else:
            self._in_memory_records[user.user_id] = user
        return user

    def get(self, user_id: str) -> UserContextRecord:
        if self._collection is not None:
            doc = self._collection.find_one({"user_id": user_id})
            return self._to_record(doc)
        if user_id not in self._in_memory_records:
            raise UserNotFoundError(f"User '{user_id}' not found")
        return self._in_memory_records[user_id]

    def list(
        self, filters: dict[str, Any] | None = None, limit: int = 100
    ) -> list[UserContextRecord]:
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

    def update_fields(self, user_id: str, fields: dict[str, Any]) -> UserContextRecord:
        payload = {**fields, "updated_at": datetime.now(timezone.utc).isoformat()}
        if self._collection is not None:
            result = self._collection.update_one({"user_id": user_id}, {"$set": payload})
            if not result.matched_count:
                raise UserNotFoundError(f"User '{user_id}' not found")
            return self.get(user_id)

        if user_id not in self._in_memory_records:
            raise UserNotFoundError(f"User '{user_id}' not found")
        data = self._in_memory_records[user_id].model_dump()
        data.update(payload)
        self._in_memory_records[user_id] = UserContextRecord.model_validate(data)
        return self._in_memory_records[user_id]

