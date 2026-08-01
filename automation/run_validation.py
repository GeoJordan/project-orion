from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from config.validator_registry import VALIDATOR_REGISTRY
from utils.logger import get_logger
from utils.report_writer import ReportWriter


logger = get_logger(__name__)

CONFIG_PATH = Path("automation/config/workbook_paths.json")
REPORT_DIRECTORY = Path("automation/reports")


def load_configuration(
    config_path: Path = CONFIG_PATH,
) -> dict[str, dict[str, Any]]:
    """Load and validate the workbook configuration registry."""

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as file:
        configuration = json.load(file)

    if not isinstance(configuration, dict):
        raise ValueError(
            "The workbook configuration must contain a JSON object."
        )

    return configuration


def create_validator(
    entry_name: str,
    entry_config: dict[str, Any],
    full_configuration: dict[str, dict[str, Any]],
):
    """Create the validator specified by one configuration entry."""

    validator_name = entry_config.get("validator")
    workbook_path = entry_config.get("workbook")
    sheet_name = entry_config.get("sheet")

    if not validator_name:
        raise ValueError(
            f"Missing validator name for configuration entry: {entry_name}"
        )

    if not workbook_path:
        raise ValueError(
            f"Missing workbook path for configuration entry: {entry_name}"
        )

    validator_class = VALIDATOR_REGISTRY.get(validator_name)

    if validator_class is None:
        raise ValueError(
            f"Validator '{validator_name}' is not registered."
        )

    common_arguments = {
        "workbook_path": Path(workbook_path),
    }

    if sheet_name:
        common_arguments["sheet_name"] = sheet_name

    # Asset validation requires the CMDB for cross-workbook checks.
    if validator_name == "AssetValidator":
        cmdb_config = full_configuration.get("cmdb")

        if not cmdb_config:
            raise ValueError(
                "The Asset Validator requires a CMDB configuration entry."
            )

        cmdb_workbook = cmdb_config.get("workbook")

        if not cmdb_workbook:
            raise ValueError(
                "The CMDB configuration is missing its workbook path."
            )

        common_arguments["cmdb_workbook_path"] = Path(
            cmdb_workbook
        )

        cmdb_sheet = cmdb_config.get("sheet")

        if cmdb_sheet:
            common_arguments["cmdb_sheet_name"] = cmdb_sheet

    return validator_class(**common_arguments)


def report_name_from_config(
    entry_name: str,
    entry_config: dict[str, Any],
) -> str:
    """Return a report name without a file extension."""

    configured_report = entry_config.get(
        "report",
        f"{entry_name}_validation.json",
    )

    return Path(configured_report).stem


def main() -> int:
    """Run all enabled Project Orion engineering validators."""

    logger.info(
        "Starting Project Orion engineering validation."
    )

    try:
        configuration = load_configuration()
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        logger.error("Unable to load configuration: %s", exc)
        return 2

    writer = ReportWriter(
        output_directory=REPORT_DIRECTORY
    )

    validation_results: dict[str, dict[str, Any]] = {}

    for entry_name, entry_config in configuration.items():
        if not entry_config.get("enabled", False):
            logger.info(
                "Skipping disabled validator: %s",
                entry_name,
            )
            continue

        validator_name = entry_config.get(
            "validator",
            "UnknownValidator",
        )

        logger.info(
            "Starting %s validation.",
            entry_name,
        )

        try:
            validator = create_validator(
                entry_name=entry_name,
                entry_config=entry_config,
                full_configuration=configuration,
            )

            summary = validator.validate()

        except (
            FileNotFoundError,
            KeyError,
            TypeError,
            ValueError,
            OSError,
        ) as exc:
            logger.error(
                "%s failed to execute: %s",
                validator_name,
                exc,
            )

            validation_results[entry_name] = {
                "workbook": entry_config.get("workbook"),
                "worksheet": entry_config.get("sheet"),
                "records": 0,
                "errors": 1,
                "warnings": 0,
                "passed": False,
                "issues": [
                    {
                        "severity": "ERROR",
                        "rule": "PLATFORM-EXEC-001",
                        "message": str(exc),
                        "row": None,
                        "ci_id": None,
                        "column": None,
                    }
                ],
            }
            continue

        validation_results[entry_name] = summary

        report_name = report_name_from_config(
            entry_name,
            entry_config,
        )

        report_path = writer.write_json(
            report_name=report_name,
            data=summary,
        )

        logger.info(
            "%s validation completed: "
            "passed=%s, errors=%s, warnings=%s",
            entry_name,
            summary["passed"],
            summary["errors"],
            summary["warnings"],
        )

        logger.info(
            "%s validation report created: %s",
            entry_name,
            report_path,
        )

    total_errors = sum(
        result["errors"]
        for result in validation_results.values()
    )

    total_warnings = sum(
        result["warnings"]
        for result in validation_results.values()
    )

    overall_passed = (
        bool(validation_results)
        and all(
            result["passed"]
            for result in validation_results.values()
        )
    )

    consolidated_summary = {
        "platform": (
            "Project Orion Engineering Validation Platform"
        ),
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
        "Engineering validation completed: "
        "passed=%s, validators=%s, errors=%s, warnings=%s",
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
