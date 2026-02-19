from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root is on sys.path so "import src..." works when running:
# python src/main.py <file.csv>
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.csv_reader import CsvError, read_value_column  # noqa: E402
from src.summary import calculate_summary  # noqa: E402


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
