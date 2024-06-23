from typing import List

class Solution(object):
    def isStartOfSeq(self, num: int, nums: set[int]) -> bool:
        return num - 1 not in nums

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        length = len(nums)
        numSet = set(nums)
        localMax = curMax = 1

        for num in nums:
            if self.isStartOfSeq(num, numSet):
                offset = 1
                while num+offset in numSet and curMax < length:
                    curMax += 1
                    offset += 1
                localMax = max(localMax, curMax)
                curMax = 1
        
        return localMax
    
sol = Solution()
res = sol.longestConsecutive([100,4,200,1,3,2])
print(res)