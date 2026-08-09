from python.common import TreeNode


class BalancedTree:
    def is_balanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if not node: return 0
            left, right = height(node.left), height(node.right)
            if left < 0 or right < 0 or abs(left - right) > 1: return -1
            return 1 + max(left, right)
        return height(root) >= 0

    def is_balanced_with_status(self, root: TreeNode | None) -> bool: return self.is_balanced(root)
