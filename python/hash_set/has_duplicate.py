from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for n in nums:
            if n not in mySet:
                mySet.add(n)
            else:
                return True
        return False