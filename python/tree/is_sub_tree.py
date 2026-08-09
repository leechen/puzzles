from python.common import TreeNode
from python.tree.is_same_tree import SameTree


class Subtree:
    def is_subtree(self, root: TreeNode | None, subroot: TreeNode | None) -> bool:
        if not subroot: return True
        if not root: return False
        return SameTree().is_same_tree(root, subroot) or self.is_subtree(root.left, subroot) or self.is_subtree(root.right, subroot)
