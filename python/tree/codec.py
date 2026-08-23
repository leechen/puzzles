
class Node:
    def __init__(self, val: int = 0, children: list['Node'] | None = None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: Node | None) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        result = []

        def dfs(node: Node) -> None:
            result.append(str(node.val))
            result.append(str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> Node | None:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        tokens = iter(data.split(","))

        def build_tree() -> Node:
            val = int(next(tokens))
            child_count = int(next(tokens))
            node = Node(val, [])
            for _ in range(child_count):
                node.children.append(build_tree())
            return node

        return build_tree()