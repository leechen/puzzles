from python.topK_elements import Solution


def test_top_k_frequent():
    assert set(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_top_k_frequent_with_ties():
    assert set(Solution().topKFrequent([4, 4, 1, 1, 2], 2)) == {1, 4}


def test_top_k_frequent_returns_all_unique_values():
    assert set(Solution().topKFrequent([1, 2, 3], 3)) == {1, 2, 3}
