class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 0

        myset = set(nums)
        res = 1

        for n in nums:
            acc = 1
            cur = n
            myset.discard(cur)

            while cur-1 in myset:
                acc += 1
                myset.remove(cur-1)
                res = max(res, acc)
                cur -= 1
            while cur+1 in myset:
                acc += 1
                myset.remove(cur+1)
                res = max(res, acc)
                cur += 1
        return res
    
sol = Solution()
res = sol.longestConsecutive([100,4,200,1,3,2])
print(res)