from __future__ import annotations

from pathlib import Path

from eidon_os.application.personal_intelligence import PersonalSnapshot
from eidon_os.domain.activity import Activity
from eidon_os.infrastructure.excel import ExcelWorkbookBuilder


class ExcelDashboardExporter:
    """Compatibility facade for the modular Excel workbook architecture."""

    def __init__(self, builder: ExcelWorkbookBuilder | None = None) -> None:
        self._builder = builder or ExcelWorkbookBuilder()

    def export(
        self,
        snapshot: PersonalSnapshot,
        activities: list[Activity],
        output_path: str | Path = "reports/eidon_dashboard.xlsx",
    ) -> Path:
        return self._builder.build(snapshot, activities, output_path)
