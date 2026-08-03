from __future__ import annotations

from datetime import datetime
from typing import Protocol

from eidon_os.domain.activity import Activity


class ActivityRepository(Protocol):
    def save(self, activity: Activity) -> None: ...
    def list_all(self) -> list[Activity]: ...
    def list_between(self, start: datetime, end: datetime) -> list[Activity]: ...
