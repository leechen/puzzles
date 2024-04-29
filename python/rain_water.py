class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        leftMax, rightMax = height[0], height[length-1]
        left = 0
        right = length - 1
        res = 0
        cur = left

        while left < right:
            minMax = min(leftMax, rightMax)

            if minMax > height[cur]:
              res += minMax - height[cur]

            if height[left] > height[right]:
                right -= 1
                rightMax = max(height[right], rightMax)
                cur = right
            else:
                left += 1
                leftMax = max(height[left], leftMax)
                cur = left

        return res
    
sol = Solution()
res = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])