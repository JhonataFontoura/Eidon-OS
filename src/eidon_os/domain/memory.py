from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Memory:
    """Represents a cataloged memory inside the Palace."""

    id: UUID
    title: str
    content: str
    category: str
    source: str | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(
        cls,
        *,
        title: str,
        content: str,
        category: str,
        source: str | None = None,
    ) -> "Memory":
        normalized_title = title.strip()
        normalized_content = content.strip()
        normalized_category = category.strip()

        if not normalized_title:
            raise ValueError("Memory title cannot be empty.")
        if not normalized_content:
            raise ValueError("Memory content cannot be empty.")
        if not normalized_category:
            raise ValueError("Memory category cannot be empty.")

        now = datetime.now(timezone.utc)
        return cls(
            id=uuid4(),
            title=normalized_title,
            content=normalized_content,
            category=normalized_category,
            source=source.strip() if source and source.strip() else None,
            created_at=now,
            updated_at=now,
        )
