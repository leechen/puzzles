// https://leetcode.com/problems/valid-sudoku/description/
// 36. Valid Sudoku

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:

// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.

public class IsValidSudokuSolution {
    public bool IsValidSudoku(char[][] board) {
        var cols = new Dictionary<int, HashSet<char>>();
        var rows = new Dictionary<int, HashSet<char>>();
        var squares = new Dictionary<(int, int), HashSet<char>>();

        for (int i = 0; i < 9; i++) {
            cols[i] = new HashSet<char>();
            rows[i] = new HashSet<char>();
        }
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                if (!squares.ContainsKey((r / 3, c / 3))) {
                    squares[(r / 3, c / 3)] = new HashSet<char>();
                }

                if (rows[r].Contains(board[r][c]) ||
                    cols[c].Contains(board[r][c]) ||
                    squares[(r / 3, c / 3)].Contains(board[r][c])) {
                    return false;
                }

                rows[r].Add(board[r][c]);
                cols[c].Add(board[r][c]);
                squares[(r / 3, c / 3)].Add(board[r][c]);
            }
        }

        return true;
    }
}
