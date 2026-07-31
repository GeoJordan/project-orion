from __future__ import annotations

from pathlib import Path

from utils.logger import get_logger
from utils.report_writer import ReportWriter
from validators.asset_validator import AssetValidator
from validators.cmdb_validator import CMDBValidator


logger = get_logger(__name__)


def main() -> int:
    """Run Project Orion engineering validations."""

    logger.info("Starting Project Orion engineering validation.")

    # Repository-relative workbook paths
    engineering_directory = Path(
        "docs/engineering/engineering-management"
    )

    cmdb_workbook_path = (
        engineering_directory / "PO-CMDB_v2.0.xlsx"
    )

    asset_workbook_path = (
        engineering_directory / "PO-Asset-Register_v1.0.xlsx"
    )

    writer = ReportWriter(
        output_directory="automation/reports"
    )

    validation_results: dict[str, dict] = {}

    # ---------------------------------------------------------
    # CMDB validation
    # ---------------------------------------------------------

    logger.info("Starting CMDB validation.")

    cmdb_validator = CMDBValidator(
        workbook_path=cmdb_workbook_path
    )

    cmdb_summary = cmdb_validator.validate()
    validation_results["cmdb"] = cmdb_summary

    cmdb_report_path = writer.write_json(
        report_name="cmdb_validation",
        data=cmdb_summary,
    )

    logger.info(
        "CMDB validation completed: passed=%s, errors=%s, warnings=%s",
        cmdb_summary["passed"],
        cmdb_summary["errors"],
        cmdb_summary["warnings"],
    )

    logger.info(
        "CMDB validation report created: %s",
        cmdb_report_path,
    )

    # ---------------------------------------------------------
    # Asset Register validation
    # ---------------------------------------------------------

    logger.info("Starting Asset Register validation.")

    asset_validator = AssetValidator(
        workbook_path=asset_workbook_path,
        cmdb_workbook_path=cmdb_workbook_path,
    )

    asset_summary = asset_validator.validate()
    validation_results["asset_register"] = asset_summary

    asset_report_path = writer.write_json(
        report_name="asset_validation",
        data=asset_summary,
    )

    logger.info(
        "Asset validation completed: passed=%s, errors=%s, warnings=%s",
        asset_summary["passed"],
        asset_summary["errors"],
        asset_summary["warnings"],
    )

    logger.info(
        "Asset validation report created: %s",
        asset_report_path,
    )

    # ---------------------------------------------------------
    # Consolidated summary
    # ---------------------------------------------------------

    total_errors = sum(
        result["errors"]
        for result in validation_results.values()
    )

    total_warnings = sum(
        result["warnings"]
        for result in validation_results.values()
    )

    overall_passed = all(
        result["passed"]
        for result in validation_results.values()
    )

    consolidated_summary = {
        "platform": "Project Orion Engineering Validation Platform",
        "validators_executed": len(validation_results),
        "overall_passed": overall_passed,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "results": validation_results,
    }

    consolidated_report_path = writer.write_json(
        report_name="engineering_validation_summary",
        data=consolidated_summary,
    )

    logger.info(
        "Engineering validation completed: passed=%s, "
        "validators=%s, errors=%s, warnings=%s",
        overall_passed,
        len(validation_results),
        total_errors,
        total_warnings,
    )

    logger.info(
        "Consolidated report created: %s",
        consolidated_report_path,
    )

    return 0 if overall_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
