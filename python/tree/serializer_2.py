from python.common import TreeNode

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode | None) -> str:
        result = []

        def dfs(node):
            if node is None:
                result.append("Nil")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None

        # Use an iterator to traverse the values in the serialized string to 
        # simplify the recursive calls and avoid using a global index variable.
        values = iter(data.split(","))

        def dfs():
            value = next(values)

            if value == "Nil":
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()