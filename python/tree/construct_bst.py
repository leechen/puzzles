from python.common import TreeNode


class BuildTree:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) != len(inorder): raise ValueError("traversals must have equal lengths")
        positions = {value: index for index, value in enumerate(inorder)}; cursor = 0
        def build(left, right):
            nonlocal cursor
            if left > right: return None
            value = preorder[cursor]; cursor += 1
            if value not in positions or not left <= positions[value] <= right: raise ValueError("invalid traversals")
            node = TreeNode(value); middle = positions[value]
            node.left = build(left, middle - 1); node.right = build(middle + 1, right)
            return node
        return build(0, len(inorder) - 1)
