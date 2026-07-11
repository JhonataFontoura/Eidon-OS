from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from eidon_os.domain.memory import Memory


class SQLiteMemoryRepository:
    """SQLite implementation of the memory repository port."""

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
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    category TEXT NOT NULL,
                    source TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_memories_category ON memories(category)"
            )

    def save(self, memory: Memory) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO memories (
                    id, title, content, category, source, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title = excluded.title,
                    content = excluded.content,
                    category = excluded.category,
                    source = excluded.source,
                    updated_at = excluded.updated_at
                """,
                (
                    str(memory.id),
                    memory.title,
                    memory.content,
                    memory.category,
                    memory.source,
                    memory.created_at.isoformat(),
                    memory.updated_at.isoformat(),
                ),
            )

    def get_by_id(self, memory_id: UUID) -> Memory | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM memories WHERE id = ?", (str(memory_id),)
            ).fetchone()
        return self._to_memory(row) if row else None

    def list_all(self) -> list[Memory]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT * FROM memories ORDER BY created_at DESC"
            ).fetchall()
        return [self._to_memory(row) for row in rows]

    @staticmethod
    def _to_memory(row: sqlite3.Row) -> Memory:
        return Memory(
            id=UUID(row["id"]),
            title=row["title"],
            content=row["content"],
            category=row["category"],
            source=row["source"],
            created_at=datetime.fromisoformat(row["created_at"]),
            updated_at=datetime.fromisoformat(row["updated_at"]),
        )
