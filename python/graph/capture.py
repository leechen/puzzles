class SurroundedRegions:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]: return
        rows, columns = len(board), len(board[0])
        def preserve(row: int, column: int) -> None:
            if not (0 <= row < rows and 0 <= column < columns) or board[row][column] != "O": return
            board[row][column] = "T"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)): preserve(row + dr, column + dc)
        for row in range(rows): preserve(row, 0); preserve(row, columns - 1)
        for column in range(columns): preserve(0, column); preserve(rows - 1, column)
        for row in range(rows):
            for column in range(columns):
                board[row][column] = "O" if board[row][column] == "T" else "X"
