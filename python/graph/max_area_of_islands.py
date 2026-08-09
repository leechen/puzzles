class MaxAreaOfIsland:
    def max_area_of_island(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, columns, seen = len(grid), len(grid[0]), set()
        def area(row: int, column: int) -> int:
            if not (0 <= row < rows and 0 <= column < columns) or not grid[row][column] or (row, column) in seen: return 0
            seen.add((row, column))
            return 1 + sum(area(row + dr, column + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        return max((area(row, column) for row in range(rows) for column in range(columns)), default=0)
