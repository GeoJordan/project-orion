from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from utils.workbook_loader import WorkbookLoader
from validators.base_validator import BaseValidator


class AssetValidator(BaseValidator):
    """Validate the Project Orion Asset Register."""

    ASSET_ID_PATTERN = re.compile(r"^AST-\d{3}$")
    CI_ID_PATTERN = re.compile(r"^CI-\d{3}$")

    REQUIRED_COLUMNS = {
        "Asset ID",
        "Linked CI ID",
        "Asset Name",
        "Category",
        "Manufacturer",
        "Model",
        "Vendor",
        "Lifecycle Status",
    }

    ALLOWED_LIFECYCLE_STATUSES = {
        "Planned",
        "Operational",
        "Maintenance",
        "Retired",
        "Disposed",
    }

    def __init__(
        self,
        workbook_path: str | Path,
        cmdb_workbook_path: str | Path,
        sheet_name: str = "01_Asset_Register",
        cmdb_sheet_name: str = "01_Configuration_Items",
    ) -> None:
        super().__init__(
            workbook_name=str(workbook_path),
            sheet_name=sheet_name,
        )

        self.workbook_path = Path(workbook_path)
        self.cmdb_workbook_path = Path(cmdb_workbook_path)
        self.cmdb_sheet_name = cmdb_sheet_name

    def validate(self) -> dict:
        dataframe = WorkbookLoader.load_excel(
            workbook_path=self.workbook_path,
            sheet_name=self.sheet_name,
            header_row=2,
        )

        self.total_records = len(dataframe)

        self.validate_required_columns(dataframe)

        if self.error_count == 0:
            self.validate_duplicate_asset_ids(dataframe)
            self.validate_asset_id_format(dataframe)
            self.validate_required_fields(dataframe)
            self.validate_linked_ci_format(dataframe)
            self.validate_linked_ci_exists(dataframe)
            self.validate_duplicate_serial_numbers(dataframe)
            self.validate_lifecycle_status(dataframe)

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
                rule="ASSET-COL-001",
                message=f"Required column is missing: {column}",
                column=column,
            )

    def validate_duplicate_asset_ids(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate duplicate Asset IDs."""

        self.validate_duplicates(
            dataframe=dataframe,
            column="Asset ID",
            rule="ASSET-ID-001",
            label="Asset ID",
            header_row=2,
        )

    def validate_asset_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["Asset ID"].items():
            asset_id = self.normalize(value)

            if (
                asset_id
                and not self.ASSET_ID_PATTERN.fullmatch(asset_id)
            ):
                self.add_error(
                    rule="ASSET-ID-002",
                    message=(
                        f"Asset ID '{asset_id}' does not match "
                        "the required format AST-###."
                    ),
                    row=self.excel_row(index, 2),
                    ci_id=asset_id,
                    column="Asset ID",
                )

    def validate_required_fields(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, record in dataframe.iterrows():
            asset_id = self.normalize(record.get("Asset ID"))

            for column in self.REQUIRED_COLUMNS:
                if self.normalize(record.get(column)):
                    continue

                self.add_error(
                    rule="ASSET-DATA-001",
                    message=f"Required field is blank: {column}",
                    row=self.excel_row(index, 2),
                    ci_id=asset_id or None,
                    column=column,
                )

    def validate_linked_ci_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["Linked CI ID"].items():
            ci_id = self.normalize(value)

            if ci_id and not self.CI_ID_PATTERN.fullmatch(ci_id):
                self.add_error(
                    rule="ASSET-CI-001",
                    message=(
                        f"Linked CI ID '{ci_id}' does not match "
                        "the required format CI-###."
                    ),
                    row=self.excel_row(index, 2),
                    ci_id=ci_id,
                    column="Linked CI ID",
                )

    def validate_linked_ci_exists(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        cmdb_dataframe = WorkbookLoader.load_excel(
            workbook_path=self.cmdb_workbook_path,
            sheet_name=self.cmdb_sheet_name,
            header_row=3,
        )

        valid_ci_ids = {
            self.normalize(value)
            for value in cmdb_dataframe["CI ID"]
            if self.normalize(value)
        }

        for index, value in dataframe["Linked CI ID"].items():
            ci_id = self.normalize(value)

            if ci_id and ci_id not in valid_ci_ids:
                self.add_error(
                    rule="ASSET-CI-002",
                    message=f"Linked CI ID does not exist in CMDB: {ci_id}",
                    row=self.excel_row(index, 2),
                    ci_id=ci_id,
                    column="Linked CI ID",
                )

    def validate_duplicate_serial_numbers(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate duplicate serial numbers."""

        self.validate_duplicates(
            dataframe=dataframe,
            column="Serial Number",
            rule="ASSET-SERIAL-001",
            label="serial number",
            header_row=2,
            id_column="Asset ID",
            severity="WARNING",
        )

    def validate_lifecycle_status(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe[
            "Lifecycle Status"
        ].items():
            status = self.normalize(value)

            if (
                status
                and status not in self.ALLOWED_LIFECYCLE_STATUSES
            ):
                self.add_error(
                    rule="ASSET-LIFE-001",
                    message=f"Invalid lifecycle status: {status}",
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        dataframe.at[index, "Asset ID"]
                    ) or None,
                    column="Lifecycle Status",
                )
