from pathlib import Path
import pandas as pd


class WorkbookLoader:
    """
    Shared workbook loader for the Project Orion Engineering Validation Platform.
    """

    @staticmethod
    def load_excel(
        workbook_path,
        sheet_name,
        header_row=3
    ):
        workbook_path = Path(workbook_path)

        if not workbook_path.exists():
            raise FileNotFoundError(
                f"Workbook not found: {workbook_path}"
            )

        try:
            df = pd.read_excel(
                workbook_path,
                sheet_name=sheet_name,
                header=header_row,
                engine="openpyxl",
                dtype=object
            )

        except ValueError:
            raise ValueError(
                f"Worksheet '{sheet_name}' not found in "
                f"{workbook_path.name}"
            )

        # Remove empty rows
        df = df.dropna(how="all")

        # Clean column names
        df.columns = [
            str(col).strip()
            for col in df.columns
        ]

        return df.reset_index(drop=True)
