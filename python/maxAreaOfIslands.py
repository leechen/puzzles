from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        length = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(length)]
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= length or j < 0 or j >= width or visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return (1 + dfs(i, j-1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1, j))

        for i in range(length):
            for j in range(width):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
        