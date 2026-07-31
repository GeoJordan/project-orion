from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional


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
