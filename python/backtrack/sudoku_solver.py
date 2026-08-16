def possible(grid: list[list[int]], y: int, x: int, n: int) -> bool:
    # Check row & column
    for i in range(9):
        if grid[y][i] == n or grid[i][x] == n:
            return False

    # Check 3x3 subgrid
    y0, x0 = (y // 3) * 3, (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False

    return True


def solve(grid: list[list[int]]) -> None:
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, y, x, n):
                        grid[y][x] = n
                        solve(grid)  # Recurse
                        grid[y][x] = 0  # Backtrack
                return

    # Print board once all cells are filled
    for row in grid:
        print(*row)


if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    solve(puzzle)