import pytest

from python.temperatures import Solution


@pytest.mark.parametrize(
    ("temperatures", "expected"),
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 30, 30], [0, 0, 0]),
        ([3, 2, 1], [0, 0, 0]),
        ([], []),
    ],
)
def test_daily_temperatures(temperatures, expected):
    assert Solution().dailyTemperatures(temperatures) == expected
