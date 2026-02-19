from __future__ import annotations

import csv
from pathlib import Path
from typing import List


class CsvError(Exception):
    pass


def read_value_column(csv_path: str | Path, column: str = "value") -> List[float]:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return []

        if column not in reader.fieldnames:
            raise CsvError(f"Missing required column: {column}")

        values: List[float] = []
        for row in reader:
            raw = (row.get(column) or "").strip()
            if raw == "":
                continue
            values.append(float(raw))
        return values
