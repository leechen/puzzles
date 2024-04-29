from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        acc = []

        def helper(openN, closeN, acc):
            if openN == closeN and openN == n:
                res.append("".join(acc))
                acc = []
                return
            if openN == n:
                acc.append(')')
                helper(openN, closeN + 1, acc)
                acc.pop()
            elif openN > closeN:
                acc.append(')')
                helper(openN, closeN + 1, acc)
                acc.pop()
                acc.append('(')
                helper(openN+1, closeN, acc)
                acc.pop()
            elif openN == closeN:
                acc.append('(')
                helper(openN+1, closeN, acc)
                acc.pop()

        helper(0, 0, acc)
        return res
    
sol = Solution()
res = sol.generateParenthesis(3)