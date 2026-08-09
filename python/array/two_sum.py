class TwoSum:
    def two_sum(self, numbers: list[int], target: int) -> list[int] | None:
        seen = {}
        for index, value in enumerate(numbers):
            if target - value in seen:
                return [seen[target - value], index]
            seen[value] = index
        return None
