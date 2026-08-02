from __future__ import annotations

import ipaddress
import re
from pathlib import Path

import pandas as pd

from utils.workbook_loader import WorkbookLoader
from validators.base_validator import BaseValidator


class IPAMValidator(BaseValidator):
    """Validate the Project Orion IP Address Register."""

    IP_ID_PATTERN = re.compile(r"^IP-\d{3}$")
    CI_ID_PATTERN = re.compile(r"^CI-\d{3}$")

    REQUIRED_COLUMNS = {
        "IP ID",
        "Linked CI ID",
        "Hostname",
        "IPv4 Address",
        "Assignment",
        "Status",
        "Subnet",
        "Gateway",
        "Device Type",
    }

    ALLOWED_ASSIGNMENTS = {
        "Static",
        "DHCP",
        "DHCP Reservation",
    }

    ALLOWED_STATUSES = {
        "Active",
        "Planned",
        "Reserved",
        "Inactive",
        "Retired",
    }

    def __init__(
        self,
        workbook_path: str | Path,
        cmdb_workbook_path: str | Path,
        sheet_name: str = "01_IP_Address_Register",
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
            self.validate_duplicate_ip_ids(dataframe)
            self.validate_ip_id_format(dataframe)
            self.validate_required_fields(dataframe)
            self.validate_linked_ci_format(dataframe)
            self.validate_linked_ci_exists(dataframe)
            self.validate_ipv4_addresses(dataframe)
            self.validate_duplicate_ipv4_addresses(dataframe)
            self.validate_subnet_membership(dataframe)
            self.validate_gateways(dataframe)
            self.validate_assignments(dataframe)
            self.validate_statuses(dataframe)
            self.validate_duplicate_hostnames(dataframe)

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
                rule="IPAM-COL-001",
                message=f"Required column is missing: {column}",
                column=column,
            )

    def validate_duplicate_ip_ids(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate duplicate IP IDs."""

        self.validate_duplicates(
            dataframe=dataframe,
            column="IP ID",
            rule="IPAM-ID-001",
            label="IP ID",
            header_row=2,
        )

    def validate_ip_id_format(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """Validate IP ID format."""

        self.validate_pattern(
            dataframe=dataframe,
            column="IP ID",
            pattern=self.IP_ID_PATTERN,
            rule="IPAM-ID-002",
            message_template=(
                "IP ID '{value}' does not match "
                "the required format IP-###."
            ),
            header_row=2,
        )

    def validate_required_fields(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, record in dataframe.iterrows():
            ip_id = self.normalize(record.get("IP ID"))

            for column in self.REQUIRED_COLUMNS:
                if self.normalize(record.get(column)):
                    continue

                self.add_error(
                    rule="IPAM-DATA-001",
                    message=f"Required field is blank: {column}",
                    row=self.excel_row(index, 2),
                    ci_id=ip_id or None,
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
                    rule="IPAM-CI-001",
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
                    rule="IPAM-CI-002",
                    message=f"Linked CI ID does not exist in CMDB: {ci_id}",
                    row=self.excel_row(index, 2),
                    ci_id=ci_id,
                    column="Linked CI ID",
                )

    def validate_ipv4_addresses(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["IPv4 Address"].items():
            address = self.normalize(value)

            if not address:
                continue

            try:
                ipaddress.IPv4Address(address)
            except ipaddress.AddressValueError:
                self.add_error(
                    rule="IPAM-IP-001",
                    message=f"Invalid IPv4 address: {address}",
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        dataframe.at[index, "IP ID"]
                    ) or None,
                    column="IPv4 Address",
                )

    def validate_duplicate_ipv4_addresses(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        addresses = (
            dataframe["IPv4 Address"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        duplicate_mask = (
            addresses.ne("")
            & addresses.duplicated(keep=False)
        )

        for index in dataframe.index[duplicate_mask]:
            address = addresses.loc[index]

            self.add_error(
                rule="IPAM-IP-002",
                message=f"Duplicate IPv4 address detected: {address}",
                row=self.excel_row(index, 2),
                ci_id=self.normalize(
                    dataframe.at[index, "IP ID"]
                ) or None,
                column="IPv4 Address",
            )

    def validate_subnet_membership(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, record in dataframe.iterrows():
            address = self.normalize(record.get("IPv4 Address"))
            subnet = self.normalize(record.get("Subnet"))

            if not address or not subnet:
                continue

            try:
                ip_address = ipaddress.IPv4Address(address)
                network = ipaddress.IPv4Network(
                    subnet,
                    strict=False,
                )
            except (
                ipaddress.AddressValueError,
                ipaddress.NetmaskValueError,
            ):
                continue

            if ip_address not in network:
                self.add_error(
                    rule="IPAM-NET-001",
                    message=(
                        f"IPv4 address {address} does not belong "
                        f"to subnet {subnet}."
                    ),
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        record.get("IP ID")
                    ) or None,
                    column="Subnet",
                )

    def validate_gateways(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["Gateway"].items():
            gateway = self.normalize(value)

            if not gateway:
                continue

            try:
                ipaddress.IPv4Address(gateway)
            except ipaddress.AddressValueError:
                self.add_error(
                    rule="IPAM-GW-001",
                    message=f"Invalid gateway address: {gateway}",
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        dataframe.at[index, "IP ID"]
                    ) or None,
                    column="Gateway",
                )

    def validate_assignments(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["Assignment"].items():
            assignment = self.normalize(value)

            if (
                assignment
                and assignment not in self.ALLOWED_ASSIGNMENTS
            ):
                self.add_error(
                    rule="IPAM-ASSIGN-001",
                    message=f"Invalid assignment type: {assignment}",
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        dataframe.at[index, "IP ID"]
                    ) or None,
                    column="Assignment",
                )

    def validate_statuses(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        for index, value in dataframe["Status"].items():
            status = self.normalize(value)

            if status and status not in self.ALLOWED_STATUSES:
                self.add_error(
                    rule="IPAM-STATUS-001",
                    message=f"Invalid IPAM status: {status}",
                    row=self.excel_row(index, 2),
                    ci_id=self.normalize(
                        dataframe.at[index, "IP ID"]
                    ) or None,
                    column="Status",
                )

    def validate_duplicate_hostnames(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        hostnames = (
            dataframe["Hostname"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.lower()
        )

        duplicate_mask = (
            hostnames.ne("")
            & hostnames.duplicated(keep=False)
        )

        for index in dataframe.index[duplicate_mask]:
            hostname = hostnames.loc[index]

            self.add_warning(
                rule="IPAM-HOST-001",
                message=f"Duplicate hostname detected: {hostname}",
                row=self.excel_row(index, 2),
                ci_id=self.normalize(
                    dataframe.at[index, "IP ID"]
                ) or None,
                column="Hostname",
            )
