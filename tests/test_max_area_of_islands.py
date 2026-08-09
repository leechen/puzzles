import pytest

from python.maxAreaOfIslands import Solution, Solution2


@pytest.mark.parametrize("implementation", [Solution, Solution2])
@pytest.mark.parametrize(
    ("grid", "expected"),
    [
        ([], 0),
        ([[]], 0),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 1),
        ([[1, 1, 0], [1, 0, 1], [0, 1, 1]], 3),
    ],
)
def test_max_area_of_island(implementation, grid, expected):
    assert implementation().maxAreaOfIsland(grid) == expected
