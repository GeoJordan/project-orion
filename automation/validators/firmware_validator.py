from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from utils.workbook_loader import WorkbookLoader
from validators.base_validator import BaseValidator


class FirmwareValidator(BaseValidator):
    """Validate the Project Orion Firmware Inventory."""

    FIRMWARE_ID_PATTERN = re.compile(r"^FW-\d{3}$")
    CI_ID_PATTERN = re.compile(r"^CI-\d{3}$")
    ASSET_ID_PATTERN = re.compile(r"^AST-\d{3}$")

    REQUIRED_COLUMNS = {
    "Firmware ID",
    "Linked CI ID",
    "Asset ID",
    "Device",
    "Vendor",
    "Current Version",
    "Approved Version",
    "Compliance",
    "Last Updated",
    "Next Review",
    }

    ALLOWED_COMPLIANCE = {
    "Compliant",
    "Non-Compliant",
    "Pending",
    "Planned",
    }

    ALLOWED_ROLLBACK = {
        "Yes",
        "No",
        "TBD",
    }

    def __init__(
        self,
        workbook_path: str | Path,
        cmdb_workbook_path: str | Path,
        asset_workbook_path: str | Path,
        sheet_name: str = "01_Firmware_Inventory",
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
        dataframe = WorkbookLoader.load_excel(
            workbook_path=self.workbook_path,
            sheet_name=self.sheet_name,
            header_row=2,
        )

        self.total_records = len(dataframe)
        self.validate_required_columns(dataframe)

        if self.error_count == 0:
            self.validate_duplicate_firmware_ids(dataframe)
            self.validate_firmware_id_format(dataframe)
            self.validate_linked_ci_format(dataframe)
            self.validate_linked_ci_exists(dataframe)
            self.validate_asset_id_format(dataframe)
            self.validate_asset_exists(dataframe)
            self.validate_required_fields(dataframe)
            self.validate_versions(dataframe)
            self.validate_compliance(dataframe)
            self.validate_dates(dataframe)

        return self.summary()

    def validate_required_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate that all required columns exist."""

        missing_columns = self.REQUIRED_COLUMNS.difference(
            dataframe.columns
        )

        for column in sorted(missing_columns):
            self.add_error(
                rule="FIRM-COL-001",
                message=f"Required column is missing: {column}",
                column=column,
            )

    def validate_duplicate_firmware_ids(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Detect duplicate Firmware IDs."""

        firmware_ids = (
            dataframe["Firmware ID"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        duplicate_mask = (
            firmware_ids.ne("")
            & firmware_ids.duplicated(keep=False)
        )

        for index in dataframe.index[duplicate_mask]:
            firmware_id = firmware_ids.loc[index]

            self.add_error(
                rule="FIRM-ID-001",
                message=f"Duplicate Firmware ID detected: {firmware_id}",
                row=index + 4,
                ci_id=firmware_id,
                column="Firmware ID",
            )

    def validate_firmware_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Firmware ID format."""

        for index, value in dataframe["Firmware ID"].items():
            firmware_id = self.normalize(value)

            if (
                firmware_id
                and not self.FIRMWARE_ID_PATTERN.fullmatch(firmware_id)
            ):
                self.add_error(
                    rule="FIRM-ID-002",
                    message=(
                        f"Firmware ID '{firmware_id}' must match FW-###."
                    ),
                    row=index + 4,
                    ci_id=firmware_id,
                    column="Firmware ID",
                )

    def validate_linked_ci_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Linked CI ID format."""

        for index, value in dataframe["Linked CI ID"].items():
            ci_id = self.normalize(value)

            if ci_id and not self.CI_ID_PATTERN.fullmatch(ci_id):
                self.add_error(
                    rule="FIRM-CI-001",
                    message=f"Linked CI ID '{ci_id}' must match CI-###.",
                    row=index + 4,
                    ci_id=ci_id,
                    column="Linked CI ID",
                )

    def validate_linked_ci_exists(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Confirm that each Linked CI ID exists in the CMDB."""

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
                    rule="FIRM-CI-002",
                    message=f"Linked CI ID does not exist in CMDB: {ci_id}",
                    row=index + 4,
                    ci_id=ci_id,
                    column="Linked CI ID",
                )

    def validate_asset_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate Asset ID format."""

        for index, value in dataframe["Asset ID"].items():
            asset_id = self.normalize(value)

            if (
                asset_id
                and not self.ASSET_ID_PATTERN.fullmatch(asset_id)
            ):
                self.add_error(
                    rule="FIRM-ASSET-001",
                    message=f"Asset ID '{asset_id}' must match AST-###.",
                    row=index + 4,
                    ci_id=asset_id,
                    column="Asset ID",
                )

    def validate_asset_exists(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Confirm that each Asset ID exists in the Asset Register."""

        asset_dataframe = WorkbookLoader.load_excel(
            workbook_path=self.asset_workbook_path,
            sheet_name=self.asset_sheet_name,
            header_row=2,
        )

        valid_asset_ids = {
            self.normalize(value)
            for value in asset_dataframe["Asset ID"]
            if self.normalize(value)
        }

        for index, value in dataframe["Asset ID"].items():
            asset_id = self.normalize(value)

            if asset_id and asset_id not in valid_asset_ids:
                self.add_error(
                    rule="FIRM-ASSET-002",
                    message=(
                        "Asset ID does not exist in Asset Register: "
                        f"{asset_id}"
                    ),
                    row=index + 4,
                    ci_id=asset_id,
                    column="Asset ID",
                )

    def validate_required_fields(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate required firmware inventory fields."""

        for index, record in dataframe.iterrows():
            firmware_id = self.normalize(
                record.get("Firmware ID")
            )

            compliance = self.normalize(
                record.get("Compliance")
            )

            for column in self.REQUIRED_COLUMNS:
                if self.normalize(record.get(column)):
                    continue

                if (compliance == "Planned"
                    and column in {
                        "Last Updated",
                        "Next Review",
                        }):
                    continue

                self.add_error(
                    rule="FIRM-DATA-001",
                    message=f"Required field is blank: {column}",
                    row=index + 4,
                    ci_id=firmware_id or None,
                    column=column,
                )

    def validate_versions(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Compare current and approved firmware versions."""

        for index, record in dataframe.iterrows():
            firmware_id = self.normalize(record.get("Firmware ID"))
            current_version = self.normalize(
                record.get("Current Version")
            )
            approved_version = self.normalize(
                record.get("Approved Version")
            )

            if (
                current_version
                and approved_version
                and current_version != approved_version
            ):
                self.add_warning(
                    rule="FIRM-VERSION-001",
                    message=(
                        f"Current Version '{current_version}' does not "
                        f"match Approved Version '{approved_version}'."
                    ),
                    row=index + 4,
                    ci_id=firmware_id or None,
                    column="Current Version",
                )

    def validate_compliance(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate firmware compliance and rollback values."""

        for index, record in dataframe.iterrows():
            firmware_id = self.normalize(record.get("Firmware ID"))
            compliance = self.normalize(record.get("Compliance"))

            if (
                compliance
                and compliance not in self.ALLOWED_COMPLIANCE
            ):
                self.add_error(
                    rule="FIRM-COMP-001",
                    message=f"Invalid compliance value: {compliance}",
                    row=index + 4,
                    ci_id=firmware_id or None,
                    column="Compliance",
                )

            if "Rollback Available" in dataframe.columns:
                rollback = self.normalize(
                    record.get("Rollback Available")
                )

                if (
                    rollback
                    and rollback not in self.ALLOWED_ROLLBACK
                ):
                    self.add_warning(
                        rule="FIRM-ROLLBACK-001",
                        message=f"Invalid rollback value: {rollback}",
                        row=index + 4,
                        ci_id=firmware_id or None,
                        column="Rollback Available",
                    )

    def validate_dates(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate firmware date fields."""

        date_columns = {
            "Release Date": "FIRM-DATE-001",
            "End of Support": "FIRM-DATE-002",
            "Last Updated": "FIRM-DATE-003",
            "Next Review": "FIRM-DATE-004",
        }

        for index, value in dataframe["End of Support"].items():
            if self.normalize(value):
                continue

        self.add_warning(
            rule="FIRM-DATE-005",
            message="End of Support date is not populated.",
            row=index + 4,
            ci_id=self.normalize(
                dataframe.at[index, "Firmware ID"]
            ) or None,
            column="End of Support",
    )

        for column, rule in date_columns.items():
            if column not in dataframe.columns:
                continue

            for index, value in dataframe[column].items():
                if self.normalize(value) == "":
                    continue

                parsed_date = pd.to_datetime(
                    value,
                    errors="coerce",
                )

                if pd.isna(parsed_date):
                    self.add_warning(
                        rule=rule,
                        message=(
                            f"Invalid or unrecognized date in "
                            f"{column}: {value}"
                        ),
                        row=index + 4,
                        ci_id=self.normalize(
                            dataframe.at[index, "Firmware ID"]
                        ) or None,
                        column=column,
                    )

    @staticmethod
    def normalize(value: object) -> str:
        """Normalize workbook values."""

        if value is None or pd.isna(value):
            return ""

        return str(value).strip()
