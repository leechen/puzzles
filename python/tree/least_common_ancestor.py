from python.common import TreeNode


class LowestCommonAncestor:
    def lowest_common_ancestor(self, root: TreeNode | None, left: TreeNode, right: TreeNode) -> TreeNode | None:
        if not root or root is left or root is right: return root
        found_left = self.lowest_common_ancestor(root.left, left, right); found_right = self.lowest_common_ancestor(root.right, left, right)
        return root if found_left and found_right else found_left or found_right
