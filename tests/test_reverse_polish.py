import pytest

from python.reversePolish import Solution


@pytest.mark.parametrize(
    ("tokens", "expected"),
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["7", "-3", "/"], -2),
        (["-7", "3", "/"], -2),
        (["5"], 5),
    ],
)
def test_eval_rpn(tokens, expected):
    assert Solution().evalRPN(tokens) == expected


def test_division_does_not_lose_precision_for_large_integers():
    dividend = 10**400 + 5
    assert Solution().evalRPN([str(dividend), "3", "/"]) == dividend // 3


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Solution().evalRPN(["1", "0", "/"])
