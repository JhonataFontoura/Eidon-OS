from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from eidon_os.domain.knowledge import Company, FileRecord, KnowledgeItem, Person, Project, Relationship


class SQLiteKnowledgeRepository:
    def __init__(self, database_path: str | Path = "data/eidon.db") -> None:
        self._database_path = Path(database_path)
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def _initialize_schema(self) -> None:
        statements = [
            """CREATE TABLE IF NOT EXISTS projects (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, description TEXT NOT NULL,
                status TEXT NOT NULL, github_url TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS files (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, path TEXT NOT NULL, media_type TEXT,
                category TEXT, sha256 TEXT, size_bytes INTEGER, summary TEXT, source TEXT,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS people (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, role TEXT, organization TEXT,
                contact TEXT, notes TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS companies (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, website TEXT, technologies TEXT,
                notes TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS knowledge_items (
                id TEXT PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL, kind TEXT NOT NULL,
                source TEXT, tags TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS relationships (
                id TEXT PRIMARY KEY, source_type TEXT NOT NULL, source_id TEXT NOT NULL,
                target_type TEXT NOT NULL, target_id TEXT NOT NULL, relation_type TEXT NOT NULL,
                notes TEXT, created_at TEXT NOT NULL
            )""",
            "CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status)",
            "CREATE INDEX IF NOT EXISTS idx_files_category ON files(category)",
            "CREATE INDEX IF NOT EXISTS idx_knowledge_kind ON knowledge_items(kind)",
            "CREATE INDEX IF NOT EXISTS idx_relationship_source ON relationships(source_type, source_id)",
            "CREATE INDEX IF NOT EXISTS idx_relationship_target ON relationships(target_type, target_id)",
        ]
        with self._connect() as connection:
            for statement in statements:
                connection.execute(statement)

    def _execute(self, statement: str, values: tuple[object, ...]) -> None:
        with self._connect() as connection:
            connection.execute(statement, values)

    def _rows(self, query: str) -> list[sqlite3.Row]:
        with self._connect() as connection:
            return connection.execute(query).fetchall()

    def save_project(self, project: Project) -> None:
        self._execute("INSERT OR REPLACE INTO projects VALUES (?, ?, ?, ?, ?, ?, ?)", (str(project.id), project.name, project.description, project.status, project.github_url, project.created_at.isoformat(), project.updated_at.isoformat()))

    def list_projects(self) -> list[Project]:
        return [Project(UUID(r["id"]), r["name"], r["description"], r["status"], r["github_url"], datetime.fromisoformat(r["created_at"]), datetime.fromisoformat(r["updated_at"])) for r in self._rows("SELECT * FROM projects ORDER BY created_at DESC")]

    def save_file(self, item: FileRecord) -> None:
        self._execute("INSERT OR REPLACE INTO files VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(item.id), item.name, item.path, item.media_type, item.category, item.sha256, item.size_bytes, item.summary, item.source, item.created_at.isoformat(), item.updated_at.isoformat()))

    def list_files(self) -> list[FileRecord]:
        return [FileRecord(UUID(r["id"]), r["name"], r["path"], r["media_type"], r["category"], r["sha256"], r["size_bytes"], r["summary"], r["source"], datetime.fromisoformat(r["created_at"]), datetime.fromisoformat(r["updated_at"])) for r in self._rows("SELECT * FROM files ORDER BY created_at DESC")]

    def save_person(self, item: Person) -> None:
        self._execute("INSERT OR REPLACE INTO people VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (str(item.id), item.name, item.role, item.organization, item.contact, item.notes, item.created_at.isoformat(), item.updated_at.isoformat()))

    def list_people(self) -> list[Person]:
        return [Person(UUID(r["id"]), r["name"], r["role"], r["organization"], r["contact"], r["notes"], datetime.fromisoformat(r["created_at"]), datetime.fromisoformat(r["updated_at"])) for r in self._rows("SELECT * FROM people ORDER BY created_at DESC")]

    def save_company(self, item: Company) -> None:
        self._execute("INSERT OR REPLACE INTO companies VALUES (?, ?, ?, ?, ?, ?, ?)", (str(item.id), item.name, item.website, item.technologies, item.notes, item.created_at.isoformat(), item.updated_at.isoformat()))

    def list_companies(self) -> list[Company]:
        return [Company(UUID(r["id"]), r["name"], r["website"], r["technologies"], r["notes"], datetime.fromisoformat(r["created_at"]), datetime.fromisoformat(r["updated_at"])) for r in self._rows("SELECT * FROM companies ORDER BY created_at DESC")]

    def save_knowledge(self, item: KnowledgeItem) -> None:
        self._execute("INSERT OR REPLACE INTO knowledge_items VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (str(item.id), item.title, item.content, item.kind, item.source, item.tags, item.created_at.isoformat(), item.updated_at.isoformat()))

    def list_knowledge(self) -> list[KnowledgeItem]:
        return [KnowledgeItem(UUID(r["id"]), r["title"], r["content"], r["kind"], r["source"], r["tags"], datetime.fromisoformat(r["created_at"]), datetime.fromisoformat(r["updated_at"])) for r in self._rows("SELECT * FROM knowledge_items ORDER BY created_at DESC")]

    def save_relationship(self, item: Relationship) -> None:
        self._execute("INSERT OR REPLACE INTO relationships VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (str(item.id), item.source_type, str(item.source_id), item.target_type, str(item.target_id), item.relation_type, item.notes, item.created_at.isoformat()))

    def list_relationships(self) -> list[Relationship]:
        return [Relationship(UUID(r["id"]), r["source_type"], UUID(r["source_id"]), r["target_type"], UUID(r["target_id"]), r["relation_type"], r["notes"], datetime.fromisoformat(r["created_at"])) for r in self._rows("SELECT * FROM relationships ORDER BY created_at DESC")]
