from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def require_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} cannot be empty")
    return normalized


@dataclass(slots=True)
class Activity:
    id: UUID
    title: str
    category: str
    description: str | None = None
    duration_minutes: int = 0
    source_type: str | None = None
    source_id: UUID | None = None
    occurred_at: datetime = field(default_factory=utc_now)
    created_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(
        cls,
        *,
        title: str,
        category: str,
        description: str | None = None,
        duration_minutes: int = 0,
        source_type: str | None = None,
        source_id: UUID | None = None,
        occurred_at: datetime | None = None,
    ) -> "Activity":
        if duration_minutes < 0:
            raise ValueError("duration_minutes cannot be negative")
        return cls(
            id=uuid4(),
            title=require_text(title, "title"),
            category=require_text(category, "category"),
            description=description.strip() if description else None,
            duration_minutes=duration_minutes,
            source_type=source_type.strip() if source_type else None,
            source_id=source_id,
            occurred_at=occurred_at or utc_now(),
        )
