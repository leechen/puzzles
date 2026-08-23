from functools import lru_cache

def num_of_paths_to_dest(n: int) -> int:
    if n <= 1:
        return 1

    # the caching technique is used to avoid recalculating the number of paths for the same (i, j) coordinates multiple times
    # without caching, it times out if n is large because the number of recursive calls grows exponentially
    @lru_cache(maxsize=None)
    def count_paths(i: int, j: int) -> int:
        # Out of bounds or crossed above diagonal (j > i)
        if i < 0 or j < 0 or j > i:
            return 0
        
        # Base case: reached start point (0, 0)
        if i == 0 and j == 0:
            return 1
        
        # Sum ways coming from left (i - 1, j) and from below (i, j - 1)
        return count_paths(i - 1, j) + count_paths(i, j - 1)

    return count_paths(n - 1, n - 1)