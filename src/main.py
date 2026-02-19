from __future__ import annotations

import sys

from src.csv_reader import CsvError, read_value_column
from src.summary import calculate_summary


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python src/main.py <path-to-csv>", file=sys.stderr)
        return 2

    csv_path = argv[1]

    try:
        values = read_value_column(csv_path, column="value")
        summary = calculate_summary(values)
    except (FileNotFoundError, CsvError) as e:
        print(str(e), file=sys.stderr)
        return 2

    print(f"Rows: {summary['count']}")
    print(f"Sum: {summary['sum']}")
    print(f"Average: {summary['average']}")
    print(f"Top 3: {summary['top_3']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
