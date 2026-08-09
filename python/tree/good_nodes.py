from python.common import TreeNode


class GoodNodes:
    def good_nodes(self, root: TreeNode | None) -> int:
        def count(node, maximum):
            if not node: return 0
            good = node.val >= maximum
            return good + count(node.left, max(maximum, node.val)) + count(node.right, max(maximum, node.val))
        return count(root, float("-inf"))
