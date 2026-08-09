import pytest

from python.rain_water import Solution, main


@pytest.mark.parametrize(
    ("heights", "expected"),
    [
        ([], 0),
        ([0], 0),
        ([1, 2, 3], 0),
        ([3, 2, 1], 0),
        ([4, 2, 0, 3, 2, 5], 9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ],
)
def test_trap(heights, expected):
    assert Solution().trap(heights) == expected


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "6\n"
