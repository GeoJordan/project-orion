from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from utils.workbook_loader import WorkbookLoader
from validators.base_validator import BaseValidator


class MaintenanceValidator(BaseValidator):
    """Validate the Project Orion Maintenance Schedule."""

    MAINTENANCE_ID_PATTERN = re.compile(r"^MNT-\d{3}$")
    CI_ID_PATTERN = re.compile(r"^CI-\d{3}$")
    ASSET_ID_PATTERN = re.compile(r"^AST-\d{3}$")

    REQUIRED_COLUMNS = {
        "Maintenance ID",
        "Linked CI ID",
        "Asset ID",
        "Maintenance Type",
        "Task",
        "Frequency",
        "Scheduled Date",
        "Owner",
        "Status",
        "Priority",
        "Estimated Duration",
        "Completion Date",
        "Related Change ID",
        "Notes",
    }

    REQUIRED_FIELDS = {
        "Maintenance ID",
        "Linked CI ID",
        "Maintenance Type",
        "Task",
        "Frequency",
        "Scheduled Date",
        "Owner",
        "Status",
        "Priority",
    }

    ALLOWED_STATUSES = {
        "Planned",
        "Scheduled",
        "In Progress",
        "Completed",
        "Deferred",
        "Cancelled",
    }

    # Initial controlled values based on the current workbook records.
    ALLOWED_FREQUENCIES = {
        "Weekly",
        "Monthly",
        "Quarterly",
    }

    ALLOWED_PRIORITIES = {
        "Critical",
        "High",
        "Medium",
        "Low",
    }

    def __init__(
        self,
        workbook_path: str | Path,
        cmdb_workbook_path: str | Path,
        asset_workbook_path: str | Path,
        sheet_name: str = "01_Maintenance_Schedule",
        cmdb_sheet_name: str = "01_Configuration_Items",
        asset_sheet_name: str = "01_Asset_Register",
    ) -> None:
        super().__init__(
            workbook_name=str(workbook_path),
            sheet_name=sheet_name,
        )

        self.workbook_path = Path(workbook_path)
        self.cmdb_workbook_path = Path(cmdb_workbook_path)
        self.asset_workbook_path = Path(asset_workbook_path)
        self.cmdb_sheet_name = cmdb_sheet_name
        self.asset_sheet_name = asset_sheet_name

    def validate(self) -> dict:
        """Run the Maintenance Schedule validation suite."""

        dataframe = WorkbookLoader.load_excel(
            workbook_path=self.workbook_path,
            sheet_name=self.sheet_name,
            header_row=2,
        )

        self.total_records = len(dataframe)

        self.validate_required_columns(dataframe)

        if self.error_count == 0:
            self.validate_duplicate_maintenance_ids(dataframe)
            self.validate_maintenance_id_format(dataframe)
            self.validate_linked_ci_format(dataframe)
            self.validate_asset_id_format(dataframe)
            self.validate_linked_ci_exists(dataframe)
            self.validate_asset_exists(dataframe)
            self.validate_required_fields(dataframe)
            self.validate_statuses(dataframe)
            self.validate_frequencies(dataframe)
            self.validate_priorities(dataframe)

        return self.summary()

    def validate_required_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate that all expected columns exist."""

        missing_columns = self.missing_columns(
            dataframe,
            self.REQUIRED_COLUMNS,
        )

        for column in missing_columns:
            self.add_error(
                rule="MAINT-COL-001",
                message=f"Required column is missing: {column}",
                column=column,
            )

    def validate_duplicate_maintenance_ids(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate duplicate Maintenance IDs."""

        self.validate_duplicates(
            dataframe=dataframe,
            column="Maintenance ID",
            rule="MAINT-ID-001",
            label="Maintenance ID",
            header_row=2,
        )

    def validate_maintenance_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Maintenance ID format."""

        self.validate_pattern(
            dataframe=dataframe,
            column="Maintenance ID",
            pattern=self.MAINTENANCE_ID_PATTERN,
            rule="MAINT-ID-002",
            message_template=(
                "Maintenance ID '{value}' does not match "
                "the required format MNT-###."
            ),
            header_row=2,
        )

    def validate_linked_ci_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Linked CI ID format."""

        self.validate_pattern(
            dataframe=dataframe,
            column="Linked CI ID",
            pattern=self.CI_ID_PATTERN,
            rule="MAINT-CI-001",
            message_template=(
                "Linked CI ID '{value}' does not match "
                "the required format CI-###."
            ),
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_asset_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate populated Asset ID values."""

        self.validate_pattern(
            dataframe=dataframe,
            column="Asset ID",
            pattern=self.ASSET_ID_PATTERN,
            rule="MAINT-ASSET-001",
            message_template=(
                "Asset ID '{value}' does not match "
                "the required format AST-###."
            ),
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_required_fields(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate mandatory maintenance fields."""

        for index, record in dataframe.iterrows():
            maintenance_id = self.normalize(
                record.get("Maintenance ID")
            )

            for column in self.REQUIRED_FIELDS:
                if self.normalize(record.get(column)):
                    continue

                self.add_error(
                    rule="MAINT-DATA-001",
                    message=f"Required field is blank: {column}",
                    row=self.excel_row(index, 2),
                    ci_id=maintenance_id or None,
                    column=column,
                )

    def validate_statuses(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate maintenance status values."""

        self.validate_allowed_values(
            dataframe=dataframe,
            column="Status",
            allowed_values=self.ALLOWED_STATUSES,
            rule="MAINT-STATUS-001",
            message_template="Invalid maintenance status: {value}",
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_frequencies(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate maintenance frequency values."""

        self.validate_allowed_values(
            dataframe=dataframe,
            column="Frequency",
            allowed_values=self.ALLOWED_FREQUENCIES,
            rule="MAINT-FREQ-001",
            message_template="Invalid maintenance frequency: {value}",
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_priorities(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate maintenance priority values."""

        self.validate_allowed_values(
            dataframe=dataframe,
            column="Priority",
            allowed_values=self.ALLOWED_PRIORITIES,
            rule="MAINT-PRIORITY-001",
            message_template="Invalid maintenance priority: {value}",
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_linked_ci_exists(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Linked CI IDs exist in the CMDB."""

        cmdb = WorkbookLoader.load_excel(
            workbook_path=self.cmdb_workbook_path,
            sheet_name=self.cmdb_sheet_name,
            header_row=3,
        )

        cmdb_ids = set(
            cmdb["CI ID"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        self.validate_reference_exists(
            dataframe=dataframe,
            reference_values=cmdb_ids,
            column="Linked CI ID",
            rule="MAINT-CMDB-001",
            message_template="Linked CI '{value}' does not exist in the CMDB.",
            header_row=2,
            id_column="Maintenance ID",
        )

    def validate_asset_exists(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Asset IDs exist in the Asset Register."""

        assets = WorkbookLoader.load_excel(
            workbook_path=self.asset_workbook_path,
            sheet_name=self.asset_sheet_name,
            header_row=2,
        )

        asset_ids = set(
            assets["Asset ID"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        self.validate_reference_exists(
            dataframe=dataframe,
            reference_values=asset_ids,
            column="Asset ID",
            rule="MAINT-ASSET-002",
            message_template="Asset '{value}' does not exist in the Asset Register.",
            header_row=2,
            id_column="Maintenance ID",
        )