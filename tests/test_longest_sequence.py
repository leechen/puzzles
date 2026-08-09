import pytest

from python.longest_sequence import Solution, main


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 1, 2], 2),
        ([], 0),
    ],
)
def test_longest_consecutive(values, expected):
    assert Solution().longestConsecutive(values) == expected


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "4\n"
