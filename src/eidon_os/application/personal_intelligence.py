from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from eidon_os.application.activity_ports import ActivityRepository
from eidon_os.application.knowledge_ports import KnowledgeRepository


@dataclass(frozen=True, slots=True)
class PersonalSnapshot:
    projects: int
    files: int
    people: int
    companies: int
    knowledge_items: int
    relationships: int
    activities: int
    total_minutes: int
    activity_categories: dict[str, int]


class PersonalAnalytics:
    def __init__(self, knowledge: KnowledgeRepository, activities: ActivityRepository) -> None:
        self._knowledge = knowledge
        self._activities = activities

    def snapshot(self) -> PersonalSnapshot:
        activity_list = self._activities.list_all()
        return PersonalSnapshot(
            projects=len(self._knowledge.list_projects()),
            files=len(self._knowledge.list_files()),
            people=len(self._knowledge.list_people()),
            companies=len(self._knowledge.list_companies()),
            knowledge_items=len(self._knowledge.list_knowledge()),
            relationships=len(self._knowledge.list_relationships()),
            activities=len(activity_list),
            total_minutes=sum(item.duration_minutes for item in activity_list),
            activity_categories=dict(Counter(item.category for item in activity_list)),
        )

    def weekly_timeline(self, now: datetime | None = None) -> list[object]:
        end = now or datetime.now(timezone.utc)
        return self._activities.list_between(end - timedelta(days=7), end)


class ReportService:
    @staticmethod
    def render_terminal(snapshot: PersonalSnapshot) -> str:
        hours, minutes = divmod(snapshot.total_minutes, 60)
        lines = [
            "Eidon OS - Personal Intelligence",
            "",
            f"Projects: {snapshot.projects}",
            f"Files: {snapshot.files}",
            f"People: {snapshot.people}",
            f"Companies: {snapshot.companies}",
            f"Knowledge items: {snapshot.knowledge_items}",
            f"Relationships: {snapshot.relationships}",
            f"Activities: {snapshot.activities}",
            f"Recorded time: {hours}h {minutes}min",
        ]
        if snapshot.activity_categories:
            lines.append("")
            lines.append("Activities by category:")
            for category, count in sorted(snapshot.activity_categories.items()):
                lines.append(f"- {category}: {count}")
        return "\n".join(lines)
