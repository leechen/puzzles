import pytest

from python.encode import Solution, main


@pytest.mark.parametrize(
    "values",
    [[], [""], ["lint", "code", "love", "you"], ["$", "12$hello", "雪"]],
)
def test_encode_decode_round_trip(values):
    solution = Solution()
    assert solution.decode(solution.encode(values)) == values


def test_main(capsys):
    main()
    assert capsys.readouterr().out.splitlines() == [
        "4$lint4$code4$love3$you",
        "['lint', 'code', 'love', 'you']",
    ]
