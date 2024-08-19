// https://leetcode.com/problems/search-a-2d-matrix/description/
// https://www.youtube.com/watch?v=Ber2pi2C0j0

public class SearchMatrixSolution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        int top = 0, bot = rows - 1;
        while (top <= bot) {
            int row = (top + bot) / 2;
            if (target > matrix[row][cols - 1]) {
                top = row + 1;
            } else if (target < matrix[row][0]) {
                bot = row - 1;
            } else {
                break;
            }
        }

        if (top > bot) {
            return false;
        }

        int targetRow = (top + bot) / 2;
        int l = 0, r = cols - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (target > matrix[targetRow][m]) {
                l = m + 1;
            } else if (target < matrix[targetRow][m]) {
                r = m - 1;
            } else {
                return true;
            }
        }

        return false;
    }

    // A little cleaner:
    public bool SearchMatrix2(int[][] matrix, int target) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        
        int top = 0, bot = rows - 1;
        
        // Binary search for the correct row
        while (top <= bot) {
            int row = (top + bot) / 2;
            if (target > matrix[row][cols - 1]) {
                top = row + 1;
            } else if (target < matrix[row][0]) {
                bot = row - 1;
            } else {
                // Binary search in the selected row
                int l = 0, r = cols - 1;
                while (l <= r) {
                    int m = (l + r) / 2;
                    if (matrix[row][m] == target) {
                        return true;
                    } else if (matrix[row][m] < target) {
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
                return false;
            }
        }
        
        return false;
    }
}