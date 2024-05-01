from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        length = len(temp)
        res = [0] * length
        stack = []

        for i, v in enumerate(temp):
            while stack and stack[-1][0] < v:
                t, index = stack.pop()
                res[index] = i - index
            stack.append([v, i])

        return res

        