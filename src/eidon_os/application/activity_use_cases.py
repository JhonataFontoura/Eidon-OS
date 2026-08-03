from __future__ import annotations

from datetime import datetime
from uuid import UUID

from eidon_os.application.activity_ports import ActivityRepository
from eidon_os.domain.activity import Activity


class ActivityService:
    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    def register(
        self,
        *,
        title: str,
        category: str,
        description: str | None = None,
        duration_minutes: int = 0,
        source_type: str | None = None,
        source_id: str | None = None,
        occurred_at: datetime | None = None,
    ) -> Activity:
        activity = Activity.create(
            title=title,
            category=category,
            description=description,
            duration_minutes=duration_minutes,
            source_type=source_type,
            source_id=UUID(source_id) if source_id else None,
            occurred_at=occurred_at,
        )
        self._repository.save(activity)
        return activity

    def list_all(self) -> list[Activity]:
        return self._repository.list_all()

    def list_between(self, start: datetime, end: datetime) -> list[Activity]:
        if start > end:
            raise ValueError("start must be before end")
        return self._repository.list_between(start, end)
