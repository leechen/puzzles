from python.common import TreeNode


class TreeNodeDistance:
    def calculate_distance(self, root: TreeNode | None, left: int, right: int) -> int:
        def path(node, target, distance=0):
            if not node: return None
            if node.val == target: return distance
            found = path(node.left, target, distance + 1)
            return found if found is not None else path(node.right, target, distance + 1)
        def lca(node):
            if not node or node.val in {left, right}: return node
            a, b = lca(node.left), lca(node.right)
            return node if a and b else a or b
        ancestor = lca(root)
        if not ancestor: raise ValueError("nodes not found")
        first, second = path(ancestor, left), path(ancestor, right)
        if first is None or second is None: raise ValueError("nodes not found")
        return first + second
