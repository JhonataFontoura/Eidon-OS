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

    def snapshot(self, *, start: datetime | None = None, end: datetime | None = None, category: str | None = None) -> PersonalSnapshot:
        activity_list = self._activities.list_all()
        if start is not None:
            activity_list = [item for item in activity_list if item.occurred_at >= start]
        if end is not None:
            activity_list = [item for item in activity_list if item.occurred_at <= end]
        if category:
            expected = category.casefold()
            activity_list = [item for item in activity_list if item.category.casefold() == expected]
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

    def monthly_timeline(self, now: datetime | None = None) -> list[object]:
        end = now or datetime.now(timezone.utc)
        start = end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return self._activities.list_between(start, end)


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
            lines.extend(["", "Activities by category:"])
            for category, count in sorted(snapshot.activity_categories.items()):
                lines.append(f"- {category}: {count}")
        return "\n".join(lines)

    @staticmethod
    def render_markdown(title: str, snapshot: PersonalSnapshot, activities: list[object]) -> str:
        hours, minutes = divmod(snapshot.total_minutes, 60)
        lines = [f"# {title}", "", f"- Atividades: **{snapshot.activities}**", f"- Tempo registrado: **{hours}h {minutes}min**", ""]
        if snapshot.activity_categories:
            lines.append("## Categorias")
            for category, count in sorted(snapshot.activity_categories.items()):
                lines.append(f"- {category}: {count}")
            lines.append("")
        lines.append("## Timeline")
        if not activities:
            lines.append("Nenhuma atividade registrada no período.")
        else:
            for item in activities:
                lines.append(f"- {item.occurred_at.date().isoformat()} — {item.title} ({item.category}, {item.duration_minutes} min)")
        return "\n".join(lines) + "\n"
