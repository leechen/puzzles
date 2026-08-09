from python.common import TreeNode


class KthSmallest:
    def kth_smallest(self, root: TreeNode | None, k: int) -> int:
        stack, current = [], root
        while stack or current:
            while current: stack.append(current); current = current.left
            current = stack.pop(); k -= 1
            if k == 0: return current.val
            current = current.right
        raise ValueError("k exceeds tree size")

    def kth_smallest_iterative(self, root: TreeNode | None, k: int) -> int: return self.kth_smallest(root, k)
