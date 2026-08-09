from python.common import TreeNode


class SameTree:
    def is_same_tree(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left or not right: return left is right
        return left.val == right.val and self.is_same_tree(left.left, right.left) and self.is_same_tree(left.right, right.right)
