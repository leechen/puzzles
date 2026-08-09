import pytest

from python.valieParenthesis import Solution, main


@pytest.mark.parametrize(
    ("pairs", "expected"),
    [
        (0, {""}),
        (1, {"()"}),
        (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
    ],
)
def test_generate_parenthesis(pairs, expected):
    assert set(Solution().generateParenthesis(pairs)) == expected


def test_main(capsys):
    main()
    assert "((()))" in capsys.readouterr().out
