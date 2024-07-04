
public class SearchMatrixSolution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int nRow = matrix.Length;
        int nCol = matrix[0].Length;

        // Find the row target is potentially in
        if (target < matrix[0][0] || target > matrix[nRow - 1][nCol - 1]) {
            return false;
        }

        int l = 0, r = nRow;
        int rmid = (l + r) / 2;

        while (rmid != l && rmid != r) {
            if (target < matrix[rmid][0]) {
                r = rmid;
            } else {
                l = rmid;
            }
            rmid = (l + r) / 2;
        }

        l = 0;
        r = nCol;
        int cmid = (l + r) / 2;

        while (target != matrix[rmid][cmid] && cmid != l && cmid != r) {
            if (target < matrix[rmid][cmid]) {
                r = cmid;
            } else {
                l = cmid;
            }
            cmid = (l + r) / 2;
        }

        return target == matrix[rmid][cmid];
    }
}
