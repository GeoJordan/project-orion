from pathlib import Path

from utils.logger import get_logger
from utils.report_writer import ReportWriter
from validators.cmdb_validator import CMDBValidator


logger = get_logger(__name__)


def main() -> int:
    logger.info("Starting Project Orion validation.")

    workbook_path = Path(
        "docs/engineering/engineering-management/"
        "PO-CMDB_v2.0.xlsx"
    )

    validator = CMDBValidator(workbook_path)
    summary = validator.validate()

    writer = ReportWriter(
        output_directory="automation/reports"
    )

    json_path = writer.write_json(
        "cmdb_validation",
        summary,
    )

    logger.info(
        "CMDB validation completed: passed=%s, errors=%s, warnings=%s",
        summary["passed"],
        summary["errors"],
        summary["warnings"],
    )
    logger.info("JSON report created: %s", json_path)

    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
