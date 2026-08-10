from __future__ import annotations

from pathlib import Path

from eidon_os.application.personal_intelligence import PersonalSnapshot
from eidon_os.domain.activity import Activity
from eidon_os.domain.goal import Goal
from eidon_os.infrastructure.excel.workbook_builder import ExcelWorkbookBuilder


class ExcelDashboardExporter:
    def export(self, snapshot: PersonalSnapshot, activities: list[Activity], output_path: str | Path = "reports/eidon_dashboard.xlsx", *, goals: list[Goal] | None = None) -> Path:
        return ExcelWorkbookBuilder().build(snapshot, activities, output_path, goals=goals or [])
