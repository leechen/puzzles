import pytest

from python.mergeIntervals import Solution


@pytest.mark.parametrize(
    ("intervals", "expected"),
    [
        ([], []),
        ([[1, 4]], [[1, 4]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[5, 7], [1, 2]], [[1, 2], [5, 7]]),
    ],
)
def test_merge(intervals, expected):
    assert Solution().merge(intervals) == expected
