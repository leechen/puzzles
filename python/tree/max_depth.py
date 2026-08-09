from python.common import TreeNode


class MaxDepth:
    def max_depth(self, root: TreeNode | None) -> int: return 0 if not root else 1 + max(self.max_depth(root.left), self.max_depth(root.right))
