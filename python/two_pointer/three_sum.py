class ThreeSum:
    def three_sum(self, numbers: list[int]) -> list[list[int]]:
        values, result = sorted(numbers), []
        for index, value in enumerate(values):
            if value > 0: break
            if index and value == values[index - 1]: continue
            left, right = index + 1, len(values) - 1
            while left < right:
                total = value + values[left] + values[right]
                if total < 0: left += 1
                elif total > 0: right -= 1
                else:
                    result.append([value, values[left], values[right]]); left += 1; right -= 1
                    while left < right and values[left] == values[left - 1]: left += 1
        return result
