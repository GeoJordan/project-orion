"""
Project Orion
Enterprise Change Register Generator

Sprint 7.2
Version 1.0
"""

from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment


class ChangeRegisterGenerator:
    """Generates the Project Orion Enterprise Change Register workbook."""

    def __init__(self):
        self.workbook = Workbook()

        # Project Orion Theme
        self.primary_fill = PatternFill("solid", fgColor="6B0F1A")
        self.secondary_fill = PatternFill("solid", fgColor="D9EAD3")

        self.title_font = Font(
            name="Calibri",
            size=22,
            bold=True,
            color="FFFFFF"
        )

        self.heading_font = Font(
            name="Calibri",
            size=14,
            bold=True
        )

        self.normal_font = Font(
            name="Calibri",
            size=11
        )

        self.center = Alignment(horizontal="center")

    def generate(self):
        """Generate the workbook."""

        self.create_home_sheet()
        self.create_change_register_sheet()
        self.create_change_history_sheet()
        self.create_cab_sheet()
        self.create_checklist_sheet()
        self.create_reference_sheet()
        self.create_revision_sheet()
        self.create_dashboard_sheet()

        output = Path(
            "docs/engineering/change-management/PO-CHANGE-REGISTER_v1.0.xlsx"
        )

        output.parent.mkdir(parents=True, exist_ok=True)

        self.workbook.save(output)

        print(f"Workbook created: {output}")

    def create_home_sheet(self):
        """Create the Home sheet."""

        sheet = self.workbook.active
        sheet.title = "00_Home"

        # ---------- Title ----------
        sheet.merge_cells("A1:F1")

        title = sheet["A1"]
        title.value = "PROJECT ORION"
        title.font = self.title_font
        title.fill = self.primary_fill
        title.alignment = self.center

        # ---------- Subtitle ----------
        sheet.merge_cells("A2:F2")

        subtitle = sheet["A2"]
        subtitle.value = "Enterprise Change Management Suite"
        subtitle.font = self.heading_font

        # ---------- Document Control ----------
        sheet["A4"] = "Document"
        sheet["B4"] = "PO-CHANGE-REGISTER_v1.0"

        sheet["A5"] = "Version"
        sheet["B5"] = "1.0"

        sheet["A6"] = "Status"
        sheet["B6"] = "Draft"

        sheet["A7"] = "Sprint"
        sheet["B7"] = "7.2"

        sheet["A8"] = "Owner"
        sheet["B8"] = "Project Orion"

        # ---------- Purpose ----------
        sheet["A10"] = "Purpose"

        sheet["A11"] = (
            "This workbook supports enterprise change management, "
            "validation, governance, and audit readiness."
        )

        # ---------- Workbook Navigation ----------
        sheet["A14"] = "Workbook Navigation"

        navigation = [
            "01_Change_Register",
            "02_Change_History",
            "03_CAB_Meetings",
            "04_Implementation_Checklist",
            "05_Reference_Data",
            "06_Revision_History",
            "07_Dashboard",
        ]

        row = 15

        for item in navigation:
            sheet.cell(row=row, column=1).value = item
            row += 1

        # ---------- Column Widths ----------
        sheet.column_dimensions["A"].width = 28
        sheet.column_dimensions["B"].width = 35
        sheet.column_dimensions["C"].width = 20
        sheet.freeze_panes = "A4"
        
    def create_change_register_sheet(self):
        self.workbook.create_sheet("01_Change_Register")

    def create_change_history_sheet(self):
        self.workbook.create_sheet("02_Change_History")

    def create_cab_sheet(self):
        self.workbook.create_sheet("03_CAB_Meetings")

    def create_checklist_sheet(self):
        self.workbook.create_sheet("04_Implementation_Checklist")

    def create_reference_sheet(self):
        self.workbook.create_sheet("05_Reference_Data")

    def create_revision_sheet(self):
        self.workbook.create_sheet("06_Revision_History")

    def create_dashboard_sheet(self):
        self.workbook.create_sheet("07_Dashboard")

if __name__ == "__main__":
    ChangeRegisterGenerator().generate()