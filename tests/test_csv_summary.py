import pytest
from src.summary import calculate_summary


def test_calculate_summary_basic():
    data = [10, 20, 30]
    result = calculate_summary(data)

    assert result["count"] == 3
    assert result["sum"] == 60
    assert result["average"] == 20
    assert result["top_3"] == [30, 20, 10]


def test_calculate_summary_empty():
    result = calculate_summary([])

    assert result["count"] == 0
    assert result["sum"] == 0
    assert result["average"] == 0
    assert result["top_3"] == []
