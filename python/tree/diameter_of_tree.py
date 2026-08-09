from python.common import TreeNode


class DiameterOfBinaryTree:
    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        diameter = 0
        def height(node):
            nonlocal diameter
            if not node: return 0
            left, right = height(node.left), height(node.right); diameter = max(diameter, left + right)
            return 1 + max(left, right)
        height(root)
        return diameter
