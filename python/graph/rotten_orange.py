from collections import deque


class RottenOranges:
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]: return 0
        queue, fresh = deque(), 0
        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                if value == 2: queue.append((row, column))
                elif value == 1: fresh += 1
        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, column + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2; fresh -= 1; queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
