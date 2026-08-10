from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from eidon_os.domain.goal import Goal


class SQLiteGoalRepository:
    def __init__(self, database_path: str | Path = "data/eidon.db") -> None:
        self._database_path = Path(database_path)
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_schema(self) -> None:
        with self._connect() as connection:
            connection.execute("""CREATE TABLE IF NOT EXISTS goals (
                id TEXT PRIMARY KEY,
                area TEXT NOT NULL,
                indicator TEXT NOT NULL,
                target REAL NOT NULL,
                unit TEXT NOT NULL,
                period TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL
            )""")
            connection.execute("CREATE INDEX IF NOT EXISTS idx_goals_area ON goals(area)")
            connection.execute("CREATE INDEX IF NOT EXISTS idx_goals_active ON goals(active)")

    def save(self, goal: Goal) -> None:
        with self._connect() as connection:
            connection.execute(
                "INSERT OR REPLACE INTO goals VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (str(goal.id), goal.area, goal.indicator, goal.target, goal.unit, goal.period, int(goal.active), goal.created_at.isoformat()),
            )

    def list_active(self) -> list[Goal]:
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM goals WHERE active = 1 ORDER BY area, indicator").fetchall()
        return [Goal(UUID(r["id"]), r["area"], r["indicator"], r["target"], r["unit"], r["period"], bool(r["active"]), datetime.fromisoformat(r["created_at"])) for r in rows]
