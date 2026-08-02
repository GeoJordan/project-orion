from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional
import re
import pandas as pd

@dataclass(slots=True)
class ValidationIssue:
    severity: str
    rule: str
    message: str
    row: Optional[int] = None
    ci_id: Optional[str] = None
    column: Optional[str] = None


class BaseValidator:
    """
    Base class for all Project Orion validators.
    """

    def __init__(self, workbook_name: str, sheet_name: str):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name
        self.issues: list[ValidationIssue] = []
        self.total_records = 0

    def add_error(
        self,
        rule,
        message,
        row=None,
        ci_id=None,
        column=None,
    ):
        self.issues.append(
            ValidationIssue(
                severity="ERROR",
                rule=rule,
                message=message,
                row=row,
                ci_id=ci_id,
                column=column,
            )
        )

    def add_warning(
        self,
        rule,
        message,
        row=None,
        ci_id=None,
        column=None,
    ):
        self.issues.append(
            ValidationIssue(
                severity="WARNING",
                rule=rule,
                message=message,
                row=row,
                ci_id=ci_id,
                column=column,
            )
        )

    @property
    def error_count(self):
        return sum(
            issue.severity == "ERROR"
            for issue in self.issues
        )

    @property
    def warning_count(self):
        return sum(
            issue.severity == "WARNING"
            for issue in self.issues
        )

    @property
    def passed(self):
        return self.error_count == 0

    def summary(self):
        return {
            "workbook": self.workbook_name,
            "worksheet": self.sheet_name,
            "records": self.total_records,
            "errors": self.error_count,
            "warnings": self.warning_count,
            "passed": self.passed,
            "issues": [
                asdict(issue)
                for issue in self.issues
            ],
        }

    @staticmethod
    def normalize(value: object) -> str:
        """
        Normalize workbook values.

        Converts NaN/None to an empty string and
        trims surrounding whitespace.
        """

        try:
            import pandas as pd

            if value is None or pd.isna(value):
                return ""

        except Exception:
            if value is None:
                return ""

        return str(value).strip()

    @staticmethod
    def excel_row(
        dataframe_index: int,
        header_row: int,
    ) -> int:
        """
        Convert a pandas index to the
        original Excel row number.
        """

        return dataframe_index + header_row + 2

    def has_column(
        self,
        dataframe,
        column: str,
    ) -> bool:

        return column in dataframe.columns

    def missing_columns(
        self,
        dataframe,
        required_columns,
    ) -> list[str]:
        """Return required columns missing from the dataframe."""

        return sorted(
            set(required_columns)
            - set(dataframe.columns)
        )

    def validate_duplicates(
    self,
    dataframe,
    column: str,
    rule: str,
    label: str,
    header_row: int,
    id_column: str | None = None,
    severity: str = "ERROR",
    ) -> None:
        """Detect duplicate non-blank values in a dataframe column."""

        if column not in dataframe.columns:
            return

        values = (
            dataframe[column]
            .fillna("")
            .astype(str)
            .str.strip()
    )

        duplicate_mask = (
            values.ne("")
            & values.duplicated(keep=False)
        )

        for index in dataframe.index[duplicate_mask]:
            value = values.loc[index]

            record_id = value

            if (
                id_column
                and id_column in dataframe.columns
            ):
                record_id = self.normalize(
                    dataframe.at[index, id_column]
                ) or None

            message = f"Duplicate {label} detected: {value}"

            issue_arguments = {
                "rule": rule,
                "message": message,
                "row": self.excel_row(index, header_row),
                "ci_id": record_id,
                "column": column,
            }

            if severity.upper() == "WARNING":
                self.add_warning(**issue_arguments)
            else:
                self.add_error(**issue_arguments)

    def validate_pattern(
    self,
    dataframe,
    column: str,
    pattern,
    rule: str,
    message_template: str,
    header_row: int,
    id_column: str | None = None,
    ) -> None:
        """
        Validate values against a regular expression.
        """

        if column not in dataframe.columns:
            return

        for index, value in dataframe[column].items():

            value = self.normalize(value)

            if not value:
                continue

            if pattern.fullmatch(value):
                continue

            record_id = value

            if (
                id_column
                and id_column in dataframe.columns
            ):
                record_id = self.normalize(
                    dataframe.at[index, id_column]
                ) or None

            self.add_error(
                rule=rule,
                message=message_template.format(value=value),
                row=self.excel_row(index, header_row),
                ci_id=record_id,
                column=column,
            )
    def validate_allowed_values(
    self,
    dataframe: pd.DataFrame,
    column: str,
    allowed_values: set[str],
    rule: str,
    message_template: str,
    header_row: int,
    id_column: str,
    severity: str = "ERROR",
    ) -> None:
        """
        Validate that column values belong to an approved set.
        """

        if not self.has_column(dataframe, column):
            return

        if not self.has_column(dataframe, id_column):
            return

        for index, value in dataframe[column].items():

            normalized = self.normalize(value)

            if not normalized:
                continue

            if normalized in allowed_values:
                continue

            identifier = self.normalize(
                dataframe.at[index, id_column]
            ) or None

            kwargs = dict(
                rule=rule,
                message=message_template.format(value=normalized),
                row=self.excel_row(index, header_row),
                ci_id=identifier,
                column=column,
            )

            if severity.upper() == "WARNING":
                self.add_warning(**kwargs)
            else:
                self.add_error(**kwargs)

    def validate_reference_exists(
        self,
        dataframe: pd.DataFrame,
        reference_values: set[str],
        column: str,
        rule: str,
        message_template: str,
        header_row: int,
        id_column: str,
        severity: str = "ERROR",
    ) -> None:
        """
        Validate that values exist in a reference dataset.
        """

        if not self.has_column(dataframe, column):
            return

        if not self.has_column(dataframe, id_column):
            return

        for index, value in dataframe[column].items():

            value = self.normalize(value)

            if not value:
                continue

            if value in reference_values:
                continue

            identifier = (
                self.normalize(dataframe.at[index, id_column])
                or None
            )

            kwargs = dict(
                rule=rule,
                message=message_template.format(value=value),
                row=self.excel_row(index, header_row),
                ci_id=identifier,
                column=column,
            )

            if severity.upper() == "WARNING":
                self.add_warning(**kwargs)
            else:
                self.add_error(**kwargs)