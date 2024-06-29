from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        freq = [ [] for i in range(length+1)]
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for key, val in counts.items():
            freq[val].append(key)

        res = []
        for i in range(length, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res
                    