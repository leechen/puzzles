from python.common import TreeNode


class ValidBST:
    def is_valid_bst(self, root: TreeNode | None) -> bool:
        def valid(node, minimum, maximum):
            return not node or minimum < node.val < maximum and valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        return valid(root, float("-inf"), float("inf"))
