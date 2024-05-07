class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRow = len(matrix)
        nCol = len(matrix[0])

        # find the row target in potentially
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        l, r = 0, nRow
        rowMid = (l+r)//2

        while rowMid != l and rowMid != r:
            if target < matrix[rowMid][0]:
                r = rowMid
            else:
                l = rowMid
            rowMid = (l+r)//2

        l, r = 0, nCol
        colMid = (l+r)//2

        while target != matrix[rowMid][colMid] and colMid != l and colMid != r:
            if target < matrix[rowMid][colMid]:
                r = colMid
            else:
                l = colMid
            colMid = (l+r)//2

        return target == matrix[rowMid][colMid]
    
sol = Solution()
res = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)