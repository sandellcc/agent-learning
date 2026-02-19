from __future__ import annotations

from typing import Any, Dict, List


def calculate_summary(values: List[float]) -> Dict[str, Any]:
    """
    Calculate basic summary stats for a list of numeric values.

    Returns dict with:
      - count: int
      - sum: float|int
      - average: float|int
      - top_3: list (descending)
    """
    count = len(values)
    total = sum(values) if count else 0
    average = (total / count) if count else 0

    top_3 = sorted(values, reverse=True)[:3] if count else []

    return {
        "count": count,
        "sum": total,
        "average": average,
        "top_3": top_3,
    }
