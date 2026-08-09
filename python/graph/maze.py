class Maze:
    def has_path(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        if not maze or not maze[0]: return False
        rows, columns, seen = len(maze), len(maze[0]), set()
        def visit(row: int, column: int) -> bool:
            if not (0 <= row < rows and 0 <= column < columns) or maze[row][column] == 1 or (row, column) in seen: return False
            if [row, column] == destination: return True
            seen.add((row, column))
            return any(visit(row + dr, column + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        return visit(*start)
