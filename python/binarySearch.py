from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        cur = (l + r)//2

        while nums[cur] != target and cur != l and cur != r:
            if nums[cur] > target:
                r = cur
            else:
                l = cur
            cur = (l + r)//2
        
        return cur if nums[cur] == target else -1
    
sol = Solution()
res = sol.search([-1,0,3,5,9,12], 2)
