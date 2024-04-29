from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return
            if open_n < n:
                helper(open_n + 1, closed_n, path + "(")
            if closed_n < open_n:
                helper(open_n, closed_n + 1, path + ")")
                
        helper(0, 0, "")
        return res
    
sol = Solution()
res = sol.generateParenthesis(3)