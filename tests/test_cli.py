import subprocess
import sys
from pathlib import Path


def test_cli_basic_csv_outputs_summary():
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / "tests" / "fixtures" / "basic.csv"

    result = subprocess.run(
        [sys.executable, str(repo_root / "src" / "main.py"), str(csv_path)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    out = result.stdout.lower()

    assert "rows" in out
    assert "sum" in out
    assert "average" in out
    assert "top" in out
