from python.common import TreeNode


class RightSideView:
    def right_side_view(self, root: TreeNode | None) -> list[int]:
        result = []
        def visit(node, depth):
            if not node: return
            if depth == len(result): result.append(node.val)
            visit(node.right, depth + 1); visit(node.left, depth + 1)
        visit(root, 0)
        return result
