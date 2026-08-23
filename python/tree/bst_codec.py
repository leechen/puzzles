from collections import deque
from python.common import TreeNode

class BSTCodec:
    def serialize(self, root: TreeNode | None) -> str:
        if not root:
            return ""
        vals: list[str] = []

        def preorder(node: TreeNode | None) -> None:
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None

        queue = deque(int(x) for x in data.split())

        def build(upper_bound: float) -> TreeNode | None:
            # Peek without popping: queue[0]
            if not queue or queue[0] > upper_bound:
                return None

            val = queue.popleft()
            node = TreeNode(val)
            node.left = build(val)
            node.right = build(upper_bound)
            return node

        return build(float('inf'))