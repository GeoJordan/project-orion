from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


class ReportWriter:
    """
    Shared reporting utility for the
    Project Orion Engineering Validation Platform.
    """

    def __init__(self, output_directory="automation/reports"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def write_json(
        self,
        report_name,
        data
    ):
        file_path = self.output_directory / f"{report_name}.json"

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        return file_path

    def write_csv(
        self,
        report_name,
        dataframe
    ):
        file_path = self.output_directory / f"{report_name}.csv"

        dataframe.to_csv(
            file_path,
            index=False
        )

        return file_path

    def timestamp(self):

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
