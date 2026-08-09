import pytest

from python.maze import describe_number, main


@pytest.mark.parametrize(
    ("number", "expected"), [(-1, "negative"), (0, "0<n<2"), (3, "n>2")]
)
def test_describe_number(number, expected):
    assert describe_number(number) == expected


def test_main_preserves_demo_output(capsys):
    main()
    assert capsys.readouterr().out.splitlines() == [
        "n>2",
        "inf",
        "[1, 2, 3, 4]",
        "[1, 2, 3]",
        "[2, 3]",
        "[2, 8, 3]",
    ]
