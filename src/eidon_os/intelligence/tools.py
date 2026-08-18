from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from typing import Any
from uuid import UUID

from eidon_os.application.activity_use_cases import ActivityService
from eidon_os.application.goal_use_cases import GoalService
from eidon_os.application.knowledge_use_cases import KnowledgeCatalog
from eidon_os.application.personal_intelligence import PersonalAnalytics
from eidon_os.infrastructure.sqlite_activity_repository import SQLiteActivityRepository
from eidon_os.infrastructure.sqlite_goal_repository import SQLiteGoalRepository
from eidon_os.infrastructure.sqlite_knowledge_repository import SQLiteKnowledgeRepository


class EidonToolRegistry:
    """Controlled tool layer between an AI provider and the Eidon Core."""

    def __init__(
        self,
        knowledge: SQLiteKnowledgeRepository,
        activities: SQLiteActivityRepository,
        goals: SQLiteGoalRepository,
    ) -> None:
        self.knowledge = knowledge
        self.activities = activities
        self.goals = goals
        self.catalog = KnowledgeCatalog(knowledge)
        self.activity_service = ActivityService(activities)
        self.goal_service = GoalService(goals)
        self.analytics = PersonalAnalytics(knowledge, activities)

    def schemas(self) -> list[dict[str, Any]]:
        return [
            self._tool("get_dashboard", "Read the current Eidon dashboard metrics.", {}),
            self._tool("list_activities", "List personal activities stored in Eidon.", {"limit": {"type": "integer", "minimum": 1, "maximum": 100}}),
            self._tool("list_goals", "List active goals stored in Eidon.", {}),
            self._tool("list_projects", "List projects stored in Eidon.", {}),
            self._tool("list_knowledge", "List knowledge items stored in Eidon.", {}),
            self._tool("create_activity", "Create a new personal activity in Eidon.", {
                "title": {"type": "string"}, "category": {"type": "string"},
                "description": {"type": ["string", "null"]},
                "duration_minutes": {"type": "integer", "minimum": 0},
                "occurred_at": {"type": ["string", "null"], "description": "ISO-8601 datetime or null"},
            }, required=["title", "category", "duration_minutes"]),
            self._tool("create_goal", "Create a new goal in Eidon.", {
                "area": {"type": "string"}, "indicator": {"type": "string"},
                "target": {"type": "number", "exclusiveMinimum": 0},
                "unit": {"type": "string"}, "period": {"type": "string"},
            }, required=["area", "indicator", "target", "unit"]),
            self._tool("create_project", "Create a project in Eidon.", {
                "name": {"type": "string"}, "description": {"type": "string"},
                "status": {"type": "string"}, "github_url": {"type": ["string", "null"]},
            }, required=["name", "description"]),
            self._tool("create_knowledge", "Store a new knowledge item in Eidon.", {
                "title": {"type": "string"}, "content": {"type": "string"},
                "kind": {"type": "string"}, "source": {"type": ["string", "null"]},
                "tags": {"type": ["string", "null"]},
            }, required=["title", "content", "kind"]),
            self._tool("delete_record", "Delete a record. This is destructive and only works when the UI explicitly authorizes destructive actions for the current message.", {
                "record_type": {"type": "string", "enum": ["activity", "goal", "project", "knowledge"]},
                "record_id": {"type": "string"},
            }, required=["record_type", "record_id"]),
        ]

    @staticmethod
    def _tool(name: str, description: str, properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
        return {
            "type": "function", "name": name, "description": description,
            "parameters": {"type": "object", "properties": properties, "required": required or [], "additionalProperties": False},
            "strict": False,
        }

    def execute(self, name: str, arguments: dict[str, Any], *, allow_destructive: bool = False) -> dict[str, Any]:
        if name == "get_dashboard":
            snapshot = self.analytics.snapshot()
            result = asdict(snapshot)
            result["total_hours"] = round(snapshot.total_minutes / 60, 1)
            return result
        if name == "list_activities":
            limit = int(arguments.get("limit", 20))
            return {"items": [self._serialize(x) for x in self.activities.list_all()[:limit]]}
        if name == "list_goals":
            return {"items": [self._serialize(x) for x in self.goals.list_active()]}
        if name == "list_projects":
            return {"items": [self._serialize(x) for x in self.knowledge.list_projects()]}
        if name == "list_knowledge":
            return {"items": [self._serialize(x) for x in self.knowledge.list_knowledge()]}
        if name == "create_activity":
            occurred_at = arguments.get("occurred_at")
            item = self.activity_service.register(
                title=arguments["title"], category=arguments["category"],
                description=arguments.get("description"),
                duration_minutes=int(arguments.get("duration_minutes", 0)),
                occurred_at=datetime.fromisoformat(occurred_at) if occurred_at else None,
            )
            return {"created": self._serialize(item)}
        if name == "create_goal":
            item = self.goal_service.create(
                area=arguments["area"], indicator=arguments["indicator"],
                target=float(arguments["target"]), unit=arguments["unit"],
                period=arguments.get("period", "monthly"),
            )
            return {"created": self._serialize(item)}
        if name == "create_project":
            item = self.catalog.create_project(
                name=arguments["name"], description=arguments["description"],
                status=arguments.get("status", "active"), github_url=arguments.get("github_url"),
            )
            return {"created": self._serialize(item)}
        if name == "create_knowledge":
            item = self.catalog.create_knowledge(
                title=arguments["title"], content=arguments["content"], kind=arguments["kind"],
                source=arguments.get("source"), tags=arguments.get("tags"),
            )
            return {"created": self._serialize(item)}
        if name == "delete_record":
            if not allow_destructive:
                return {"deleted": False, "requires_confirmation": True, "message": "Enable destructive actions in the Eidon UI and send the request again."}
            record_id = UUID(arguments["record_id"])
            record_type = arguments["record_type"]
            methods = {
                "activity": self.activities.delete,
                "goal": self.goals.delete,
                "project": self.knowledge.delete_project,
                "knowledge": self.knowledge.delete_knowledge,
            }
            return {"deleted": methods[record_type](record_id), "record_type": record_type, "record_id": str(record_id)}
        raise ValueError(f"Unknown Eidon tool: {name}")

    @staticmethod
    def _serialize(value: Any) -> dict[str, Any]:
        raw = asdict(value)
        return {k: (str(v) if isinstance(v, UUID) else v.isoformat() if isinstance(v, datetime) else v) for k, v in raw.items()}
