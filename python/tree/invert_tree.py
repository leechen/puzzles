from python.common import TreeNode


class InvertTree:
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        if root: root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root
