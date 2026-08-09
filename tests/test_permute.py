from python.permute import Solution


def test_permute_three_values():
    result = Solution().permute([1, 2, 3])
    assert len(result) == 6
    assert {tuple(permutation) for permutation in result} == {
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    }


def test_permute_empty_input():
    assert Solution().permute([]) == [[]]
