from __future__ import annotations

from collections import Counter
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

from eidon_os.application.personal_intelligence import PersonalSnapshot
from eidon_os.domain.activity import Activity
from eidon_os.infrastructure.excel.data_builders import GeneralRow, build_general_rows, filter_by_area


class ExcelWorkbookBuilder:
    AREAS = ("Estudos", "Projetos", "Academia de Código", "Carreira")

    def build(
        self,
        snapshot: PersonalSnapshot,
        activities: list[Activity],
        output_path: str | Path,
    ) -> Path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = build_general_rows(activities)

        workbook = Workbook()
        dashboard = workbook.active
        dashboard.title = "Dashboard Geral"

        self._build_dashboard(dashboard, snapshot, rows)
        self._build_goals(workbook)
        for area in self.AREAS:
            self._build_area_sheet(workbook, area, filter_by_area(rows, area))
        self._build_general_base(workbook, rows)
        self._build_settings(workbook)
        self._build_instructions(workbook)

        workbook.save(path)
        return path

    def _build_dashboard(self, sheet, snapshot: PersonalSnapshot, rows: list[GeneralRow]) -> None:
        sheet["A1"] = "Eidon OS — Dashboard Geral"
        sheet["A1"].font = Font(size=18, bold=True)
        sheet["A2"] = "Visão consolidada de estudos, projetos, carreira e Academia de Código."

        metrics = [
            ("Projetos cadastrados", snapshot.projects),
            ("Conhecimentos", snapshot.knowledge_items),
            ("Atividades", snapshot.activities),
            ("Minutos registrados", snapshot.total_minutes),
            ("Horas registradas", round(snapshot.total_minutes / 60, 1)),
            ("Dias ativos", len({row.date.date() for row in rows})),
        ]
        for index, (label, value) in enumerate(metrics, start=4):
            sheet.cell(index, 1, label)
            sheet.cell(index, 2, value)

        counts = Counter(row.area for row in rows)
        sheet["D3"] = "Área"
        sheet["E3"] = "Atividades"
        for index, area in enumerate(self.AREAS, start=4):
            sheet.cell(index, 4, area)
            sheet.cell(index, 5, counts.get(area, 0))

        chart = BarChart()
        chart.title = "Atividades por área"
        chart.y_axis.title = "Quantidade"
        data = Reference(sheet, min_col=5, min_row=3, max_row=3 + len(self.AREAS))
        labels = Reference(sheet, min_col=4, min_row=4, max_row=3 + len(self.AREAS))
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(labels)
        sheet.add_chart(chart, "G3")
        self._format_header(sheet, 3, 4, 5)
        sheet.column_dimensions["A"].width = 24
        sheet.column_dimensions["B"].width = 18

    def _build_goals(self, workbook: Workbook) -> None:
        sheet = workbook.create_sheet("Metas")
        sheet.append(["Área", "Indicador", "Meta mensal", "Realizado", "Progresso"])
        goals = [
            ("Academia de Código", "Desafios concluídos", 40),
            ("Academia de Código", "Horas de estudo", 25),
            ("Academia de Código", "Plataformas utilizadas", 4),
            ("Academia de Código", "Tecnologias praticadas", 3),
        ]
        for row_index, (area, indicator, target) in enumerate(goals, start=2):
            sheet.append([area, indicator, target, 0, f'=IFERROR(D{row_index}/C{row_index},0)'])
            sheet.cell(row_index, 5).number_format = "0%"
        self._format_header(sheet, 1, 1, 5)
        self._add_table(sheet, "MetasTable")
        self._fit_columns(sheet)

    def _build_area_sheet(self, workbook: Workbook, area: str, rows: list[GeneralRow]) -> None:
        sheet = workbook.create_sheet(area[:31])
        sheet.append(["Data", "Atividade", "Categoria", "Minutos", "Origem", "Status", "Descrição"])
        for row in rows:
            sheet.append([
                row.date.replace(tzinfo=None), row.activity, row.category, row.minutes,
                row.origin, row.status, row.description,
            ])
        self._format_header(sheet, 1, 1, 7)
        self._add_table(sheet, self._table_name(area))
        self._fit_columns(sheet)

    def _build_general_base(self, workbook: Workbook, rows: list[GeneralRow]) -> None:
        sheet = workbook.create_sheet("Base Geral")
        sheet.append(["Data", "Área", "Atividade", "Categoria", "Minutos", "Origem", "Status", "Descrição"])
        for row in rows:
            sheet.append([
                row.date.replace(tzinfo=None), row.area, row.activity, row.category,
                row.minutes, row.origin, row.status, row.description,
            ])
        self._format_header(sheet, 1, 1, 8)
        self._add_table(sheet, "BaseGeralTable")
        self._fit_columns(sheet)

    def _build_settings(self, workbook: Workbook) -> None:
        sheet = workbook.create_sheet("Listas e Configurações")
        sheet.append(["Áreas", "Status"])
        statuses = ("Planejado", "Em andamento", "Concluído", "Pausado")
        for index in range(max(len(self.AREAS), len(statuses))):
            sheet.append([
                self.AREAS[index] if index < len(self.AREAS) else None,
                statuses[index] if index < len(statuses) else None,
            ])
        self._format_header(sheet, 1, 1, 2)
        self._fit_columns(sheet)

    def _build_instructions(self, workbook: Workbook) -> None:
        sheet = workbook.create_sheet("Instruções")
        instructions = [
            "O Dashboard Geral é apenas uma camada de visualização.",
            "Registre informações nas áreas específicas ou no banco SQLite do Eidon.",
            "A Base Geral consolida os campos comuns de todas as áreas.",
            "Estudos, Projetos, Academia de Código e Carreira possuem abas independentes.",
            "Execute novamente 'eidon dashboard-export' para atualizar o arquivo a partir do SQLite.",
        ]
        sheet["A1"] = "Como usar o Dashboard"
        sheet["A1"].font = Font(size=16, bold=True)
        for index, text in enumerate(instructions, start=3):
            sheet.cell(index, 1, f"{index - 2}. {text}")
        sheet.column_dimensions["A"].width = 100
        sheet.alignment = Alignment(wrap_text=True)

    @staticmethod
    def _format_header(sheet, row: int, start_column: int, end_column: int) -> None:
        fill = PatternFill("solid", fgColor="1F4E78")
        for column in range(start_column, end_column + 1):
            cell = sheet.cell(row, column)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = fill
            cell.alignment = Alignment(horizontal="center")

    @staticmethod
    def _add_table(sheet, name: str) -> None:
        if sheet.max_row < 2:
            sheet.append([None] * sheet.max_column)
        reference = f"A1:{sheet.cell(sheet.max_row, sheet.max_column).coordinate}"
        table = Table(displayName=name, ref=reference)
        table.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium2",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=False,
        )
        sheet.add_table(table)

    @staticmethod
    def _fit_columns(sheet) -> None:
        for column_cells in sheet.columns:
            width = min(max(len(str(cell.value or "")) for cell in column_cells) + 2, 45)
            sheet.column_dimensions[column_cells[0].column_letter].width = width

    @staticmethod
    def _table_name(area: str) -> str:
        replacements = str.maketrans("áàãâéêíóôõúçÁÀÃÂÉÊÍÓÔÕÚÇ ", "aaaaeeiooou cAAAAEEIOOOUC_")
        normalized = area.translate(replacements).replace("_", "")
        return f"{normalized}Table"
