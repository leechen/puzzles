class RotatedArraySearch:
    def search(self, numbers: list[int], target: int) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            middle = (left + right) // 2
            if numbers[middle] == target: return middle
            if numbers[left] <= numbers[middle]:
                if numbers[left] <= target < numbers[middle]: right = middle - 1
                else: left = middle + 1
            elif numbers[middle] < target <= numbers[right]: left = middle + 1
            else: right = middle - 1
        return -1
