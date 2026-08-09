from python.common import TreeNode


class LowestCommonAncestorBST:
    def lowest_common_ancestor(self, root: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
        if left.val < root.val and right.val < root.val: return self.lowest_common_ancestor(root.left, left, right)
        if left.val > root.val and right.val > root.val: return self.lowest_common_ancestor(root.right, left, right)
        return root

    def lowest_common_ancestor_iterative(self, root: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
        while (left.val - root.val) * (right.val - root.val) > 0: root = root.left if left.val < root.val else root.right
        return root
