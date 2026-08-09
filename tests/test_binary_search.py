import pytest

from python.binarySearch import Solution, main


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([1], 1, 0),
        ([1, 3], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 2, -1),
        ([], 2, -1),
    ],
)
def test_search(nums, target, expected):
    assert Solution().search(nums, target) == expected


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "5\n"
