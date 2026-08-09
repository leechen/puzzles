from python.common import TreeNode


class MaxPathSum:
    def max_path_sum(self, root: TreeNode | None) -> int:
        if not root: raise ValueError("root is required")
        best = float("-inf")
        def gain(node):
            nonlocal best
            if not node: return 0
            left, right = max(gain(node.left), 0), max(gain(node.right), 0); best = max(best, node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return int(best)
