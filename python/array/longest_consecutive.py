class LongestConsecutive:
    def longest_consecutive(self, numbers: list[int]) -> int:
        values = set(numbers)
        best = 0
        for value in values:
            if value - 1 not in values:
                length = 1
                while value + length in values:
                    length += 1
                best = max(best, length)
        return best
