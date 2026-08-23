from python.common import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid], self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid+1:]))
            return root

    # more efficient version without slicing the array
    def sortedArrayToBST2(self, nums: list[int]) -> TreeNode | None:
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)