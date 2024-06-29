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
        

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area