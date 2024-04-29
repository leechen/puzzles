class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {'+', '-', '*', '/'}
        
        for t in tokens:
            if t in ops:
                op1 = stack.pop()
                op2 = stack.pop()
                val = 0
                match t:
                    case '+':
                        val = op1 + op2
                    case '-':
                        val = op2 - op1
                    case '*':
                        val = op1 * op2
                    case '/':
                        val = op2/op1
                stack.append(int(val))
            else:
                stack.append(int(t))
        return stack.pop()
        