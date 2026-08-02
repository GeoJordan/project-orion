from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from validators.base_validator import BaseValidator
from utils.workbook_loader import WorkbookLoader


class CMDBValidator(BaseValidator):
    """Validate the Project Orion CMDB workbook."""

    REQUIRED_COLUMNS = {
        "CI ID",
        "Asset Name",
        "CI Category",
        "CI Type",
        "Operational Status",
        "Lifecycle Status",
        "Criticality",
    }

    ALLOWED_OPERATIONAL_STATUSES = {
        "Planned",
        "Active",
        "Maintenance",
        "Offline",
        "Retired",
    }

    CI_ID_PATTERN = re.compile(r"^CI-\d{3}$")

    def __init__(
        self,
        workbook_path: str | Path,
        sheet_name: str = "01_Configuration_Items",
    ) -> None:
        super().__init__(
            workbook_name=str(workbook_path),
            sheet_name=sheet_name,
        )
        self.workbook_path = Path(workbook_path)

    def validate(self) -> dict:
        dataframe = WorkbookLoader.load_excel(
            workbook_path=self.workbook_path,
            sheet_name=self.sheet_name,
            header_row=3,
        )

        self.total_records = len(dataframe)

        self.validate_required_columns(dataframe)

        if self.error_count == 0:
            self.validate_duplicate_ci_ids(dataframe)
            self.validate_ci_id_format(dataframe)
            self.validate_required_fields(dataframe)
            self.validate_status(dataframe)

        return self.summary()

    def validate_required_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        missing_columns = self.missing_columns(
            dataframe,
            self.REQUIRED_COLUMNS,
        )

        for column in sorted(missing_columns):
            self.add_error(
                rule="CMDB-COL-001",
                message=f"Required column is missing: {column}",
                column=column,
            )

    def validate_duplicate_ci_ids(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate duplicate CI IDs."""

        self.validate_duplicates(
            dataframe=dataframe,
            column="CI ID",
            rule="CMDB-ID-001",
            label="CI ID",
            header_row=3,
    )

    def validate_ci_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate CI ID format."""

        self.validate_pattern(
            dataframe=dataframe,
            column="CI ID",
            pattern=self.CI_ID_PATTERN,
            rule="CMDB-ID-002",
            message_template=(
                "CI ID '{value}' does not match "
                "the required format CI-###."
            ),
            header_row=3,
    )

    def validate_required_fields(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, record in dataframe.iterrows():
            ci_id = self.normalize(record.get("CI ID"))

            for column in self.REQUIRED_COLUMNS:
                if self.normalize(record.get(column)):
                    continue

                self.add_error(
                    rule="CMDB-DATA-001",
                    message=f"Required field is blank: {column}",
                    row=self.excel_row(index, 3),
                    ci_id=ci_id or None,
                    column=column,
                )

    def validate_status(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate operational status."""

        self.validate_allowed_values(
            dataframe=dataframe,
            column="Operational Status",
            allowed_values=self.ALLOWED_OPERATIONAL_STATUSES,
            rule="CMDB-STATUS-001",
            message_template="Invalid operational status: {value}",
            header_row=3,
            id_column="CI ID",
        )