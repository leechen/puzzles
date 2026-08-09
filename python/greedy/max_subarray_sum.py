class MaximumSubarray:
    def max_subarray(self, numbers: list[int]) -> int:
        if not numbers: return 0
        current = best = numbers[0]
        for value in numbers[1:]: current = max(value, current + value); best = max(best, current)
        return best
