from collections import deque
from python.common import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        values = []
        def visit(node):
            if not node: values.append("N"); return
            values.append(str(node.val)); visit(node.left); visit(node.right)
        visit(root)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode | None:
        values = deque(data.split(","))
        def visit():
            value = values.popleft()
            if value == "N": return None
            node = TreeNode(int(value)); node.left = visit(); node.right = visit(); return node
        root = visit()
        if values: raise ValueError("invalid serialized tree")
        return root
