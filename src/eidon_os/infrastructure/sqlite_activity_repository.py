from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from eidon_os.domain.activity import Activity
from eidon_os.infrastructure.sqlite_connection import sqlite_connection


class SQLiteActivityRepository:
    def __init__(self, database_path: str | Path = "data/eidon.db") -> None:
        self._database_path = Path(database_path)
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_schema()

    def _connection(self):
        return sqlite_connection(self._database_path)

    def _initialize_schema(self) -> None:
        with self._connection() as connection:
            connection.execute(
                """CREATE TABLE IF NOT EXISTS activities (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    duration_minutes INTEGER NOT NULL DEFAULT 0,
                    source_type TEXT,
                    source_id TEXT,
                    occurred_at TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )"""
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_activities_occurred_at ON activities(occurred_at)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_activities_category ON activities(category)"
            )

    def save(self, activity: Activity) -> None:
        with self._connection() as connection:
            connection.execute(
                "INSERT OR REPLACE INTO activities VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    str(activity.id), activity.title, activity.category,
                    activity.description, activity.duration_minutes, activity.source_type,
                    str(activity.source_id) if activity.source_id else None,
                    activity.occurred_at.isoformat(), activity.created_at.isoformat(),
                ),
            )

    def list_all(self) -> list[Activity]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT * FROM activities ORDER BY occurred_at DESC"
            ).fetchall()
        return [self._to_entity(row) for row in rows]

    def list_between(self, start: datetime, end: datetime) -> list[Activity]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT * FROM activities WHERE occurred_at BETWEEN ? AND ? ORDER BY occurred_at DESC",
                (start.isoformat(), end.isoformat()),
            ).fetchall()
        return [self._to_entity(row) for row in rows]

    @staticmethod
    def _to_entity(row: sqlite3.Row) -> Activity:
        return Activity(
            id=UUID(row["id"]), title=row["title"], category=row["category"],
            description=row["description"], duration_minutes=row["duration_minutes"],
            source_type=row["source_type"],
            source_id=UUID(row["source_id"]) if row["source_id"] else None,
            occurred_at=datetime.fromisoformat(row["occurred_at"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )
