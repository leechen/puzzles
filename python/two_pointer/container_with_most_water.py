class ContainerWithMostWater:
    def max_area(self, heights: list[int]) -> int:
        left, right, best = 0, len(heights) - 1, 0
        while left < right:
            best = max(best, (right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]: left += 1
            else: right -= 1
        return best
