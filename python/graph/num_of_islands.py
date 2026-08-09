class NumberOfIslands:
    def num_islands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]: return 0
        rows, columns, seen = len(grid), len(grid[0]), set()
        def visit(row: int, column: int) -> None:
            if not (0 <= row < rows and 0 <= column < columns) or grid[row][column] == "0" or (row, column) in seen: return
            seen.add((row, column))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)): visit(row + dr, column + dc)
        count = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in seen: count += 1; visit(row, column)
        return count
