from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from eidon_os.application.activity_use_cases import ActivityService
from eidon_os.application.goal_use_cases import GoalService
from eidon_os.application.knowledge_use_cases import KnowledgeCatalog
from eidon_os.application.personal_intelligence import PersonalAnalytics, ReportService
from eidon_os.application.use_cases import CreateMemory, ListMemories
from eidon_os.infrastructure.excel_dashboard import ExcelDashboardExporter
from eidon_os.infrastructure.sqlite_activity_repository import SQLiteActivityRepository
from eidon_os.infrastructure.sqlite_goal_repository import SQLiteGoalRepository
from eidon_os.infrastructure.sqlite_knowledge_repository import SQLiteKnowledgeRepository
from eidon_os.infrastructure.sqlite_repository import SQLiteMemoryRepository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Eidon OS local knowledge manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    memory_add = subparsers.add_parser("add", help="Catalog a new memory")
    memory_add.add_argument("--title", required=True); memory_add.add_argument("--content", required=True); memory_add.add_argument("--category", required=True); memory_add.add_argument("--source")
    subparsers.add_parser("list", help="List cataloged memories")

    project_add = subparsers.add_parser("project-add", help="Create a project")
    project_add.add_argument("--name", required=True); project_add.add_argument("--description", required=True); project_add.add_argument("--status", default="active"); project_add.add_argument("--github-url")
    subparsers.add_parser("project-list", help="List projects")

    file_add = subparsers.add_parser("file-add", help="Catalog file metadata")
    file_add.add_argument("--name", required=True); file_add.add_argument("--path", required=True); file_add.add_argument("--media-type"); file_add.add_argument("--category"); file_add.add_argument("--summary"); file_add.add_argument("--source")
    subparsers.add_parser("file-list", help="List cataloged files")

    person_add = subparsers.add_parser("person-add", help="Catalog a person")
    person_add.add_argument("--name", required=True); person_add.add_argument("--role"); person_add.add_argument("--organization"); person_add.add_argument("--contact"); person_add.add_argument("--notes")
    subparsers.add_parser("person-list", help="List people")

    company_add = subparsers.add_parser("company-add", help="Catalog a company")
    company_add.add_argument("--name", required=True); company_add.add_argument("--website"); company_add.add_argument("--technologies"); company_add.add_argument("--notes")
    subparsers.add_parser("company-list", help="List companies")

    knowledge_add = subparsers.add_parser("knowledge-add", help="Catalog knowledge")
    knowledge_add.add_argument("--title", required=True); knowledge_add.add_argument("--content", required=True); knowledge_add.add_argument("--kind", required=True); knowledge_add.add_argument("--source"); knowledge_add.add_argument("--tags")
    subparsers.add_parser("knowledge-list", help="List knowledge items")

    relation_add = subparsers.add_parser("relation-add", help="Relate two cataloged records")
    relation_add.add_argument("--source-type", required=True); relation_add.add_argument("--source-id", required=True); relation_add.add_argument("--target-type", required=True); relation_add.add_argument("--target-id", required=True); relation_add.add_argument("--relation-type", required=True); relation_add.add_argument("--notes")
    subparsers.add_parser("relation-list", help="List relationships")

    activity_add = subparsers.add_parser("activity-add", help="Register a personal activity")
    activity_add.add_argument("--title", required=True); activity_add.add_argument("--category", required=True); activity_add.add_argument("--description"); activity_add.add_argument("--duration-minutes", type=int, default=0); activity_add.add_argument("--source-type"); activity_add.add_argument("--source-id"); activity_add.add_argument("--occurred-at", help="ISO-8601 datetime")
    subparsers.add_parser("activity-list", help="List personal activities")

    goal_add = subparsers.add_parser("goal-add", help="Create a personal goal")
    goal_add.add_argument("--area", required=True); goal_add.add_argument("--indicator", required=True); goal_add.add_argument("--target", type=float, required=True); goal_add.add_argument("--unit", required=True); goal_add.add_argument("--period", default="monthly")
    subparsers.add_parser("goal-list", help="List active goals")

    dashboard = subparsers.add_parser("dashboard", help="Show the terminal dashboard")
    dashboard.add_argument("--category"); dashboard.add_argument("--start"); dashboard.add_argument("--end")
    dashboard_export = subparsers.add_parser("dashboard-export", help="Export the Excel dashboard")
    dashboard_export.add_argument("--output", default="reports/eidon_dashboard.xlsx")

    report = subparsers.add_parser("report", help="Generate Markdown progress reports")
    report.add_argument("period", choices=("weekly", "monthly")); report.add_argument("--output")
    return parser


def print_records(records: list[object], label: str) -> None:
    if not records:
        print(f"No {label} cataloged."); return
    for record in records:
        name = getattr(record, "name", None) or getattr(record, "title", None) or getattr(record, "indicator", None) or getattr(record, "relation_type", "record")
        print(f"{name} ({getattr(record, 'id')})")


def parse_date(value: str | None) -> datetime | None:
    if not value: return None
    parsed = datetime.fromisoformat(value)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def main() -> None:
    args = build_parser().parse_args()
    if args.command in {"add", "list"}:
        repository = SQLiteMemoryRepository()
        if args.command == "add":
            memory = CreateMemory(repository).execute(title=args.title, content=args.content, category=args.category, source=args.source)
            print(f"Memory cataloged: {memory.id} - {memory.title}")
        else: print_records(ListMemories(repository).execute(), "memories")
        return

    knowledge_repository = SQLiteKnowledgeRepository(); activity_repository = SQLiteActivityRepository(); goal_repository = SQLiteGoalRepository()
    catalog = KnowledgeCatalog(knowledge_repository); activity_service = ActivityService(activity_repository); goal_service = GoalService(goal_repository)

    if args.command == "activity-add":
        item = activity_service.register(title=args.title, category=args.category, description=args.description, duration_minutes=args.duration_minutes, source_type=args.source_type, source_id=args.source_id, occurred_at=parse_date(args.occurred_at)); print(f"Activity registered: {item.id}"); return
    if args.command == "activity-list": print_records(activity_service.list_all(), "activities"); return
    if args.command == "goal-add":
        item = goal_service.create(area=args.area, indicator=args.indicator, target=args.target, unit=args.unit, period=args.period); print(f"Goal created: {item.id}"); return
    if args.command == "goal-list": print_records(goal_service.list_active(), "goals"); return

    analytics = PersonalAnalytics(knowledge_repository, activity_repository)
    if args.command == "dashboard":
        print(ReportService.render_terminal(analytics.snapshot(start=parse_date(args.start), end=parse_date(args.end), category=args.category))); return
    if args.command == "dashboard-export":
        path = ExcelDashboardExporter().export(analytics.snapshot(), activity_repository.list_all(), args.output, goals=goal_service.list_active()); print(f"Dashboard exported: {path}"); return
    if args.command == "report":
        now = datetime.now(timezone.utc)
        activities = analytics.weekly_timeline(now) if args.period == "weekly" else analytics.monthly_timeline(now)
        if activities:
            start = min(item.occurred_at for item in activities); end = max(item.occurred_at for item in activities)
        else:
            start = now; end = now
        snapshot = analytics.snapshot(start=start, end=end)
        title = "Eidon OS — Relatório Semanal" if args.period == "weekly" else "Eidon OS — Relatório Mensal"
        text = ReportService.render_markdown(title, snapshot, activities)
        output = Path(args.output or f"reports/{args.period}.md"); output.parent.mkdir(parents=True, exist_ok=True); output.write_text(text, encoding="utf-8"); print(f"Report exported: {output}"); return

    if args.command == "project-add": item = catalog.create_project(name=args.name, description=args.description, status=args.status, github_url=args.github_url)
    elif args.command == "project-list": print_records(knowledge_repository.list_projects(), "projects"); return
    elif args.command == "file-add": item = catalog.create_file(name=args.name, path=args.path, media_type=args.media_type, category=args.category, summary=args.summary, source=args.source)
    elif args.command == "file-list": print_records(knowledge_repository.list_files(), "files"); return
    elif args.command == "person-add": item = catalog.create_person(name=args.name, role=args.role, organization=args.organization, contact=args.contact, notes=args.notes)
    elif args.command == "person-list": print_records(knowledge_repository.list_people(), "people"); return
    elif args.command == "company-add": item = catalog.create_company(name=args.name, website=args.website, technologies=args.technologies, notes=args.notes)
    elif args.command == "company-list": print_records(knowledge_repository.list_companies(), "companies"); return
    elif args.command == "knowledge-add": item = catalog.create_knowledge(title=args.title, content=args.content, kind=args.kind, source=args.source, tags=args.tags)
    elif args.command == "knowledge-list": print_records(knowledge_repository.list_knowledge(), "knowledge items"); return
    elif args.command == "relation-add": item = catalog.create_relationship(source_type=args.source_type, source_id=args.source_id, target_type=args.target_type, target_id=args.target_id, relation_type=args.relation_type, notes=args.notes)
    else: print_records(knowledge_repository.list_relationships(), "relationships"); return

    activity_service.register(title=f"{args.command}: {getattr(item, 'name', None) or getattr(item, 'title', None) or item.id}", category="Sistema", description="Atividade registrada automaticamente pelo Eidon OS.", source_type=args.command.replace("-add", ""), source_id=str(item.id))
    print(f"Cataloged: {item.id}")
