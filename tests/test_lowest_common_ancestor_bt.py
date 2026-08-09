from python.lowestCommonAncestorBT import Solution


def test_binary_tree_lca_for_split_nodes(bst):
    assert Solution().lowestCommonAncestor(
        bst, bst.left.right.left, bst.right.left
    ) is bst


def test_binary_tree_lca_when_one_node_is_ancestor(bst):
    assert Solution().lowestCommonAncestor(bst, bst.left, bst.left.right.right) is bst.left


def test_binary_tree_lca_rejects_missing_inputs(bst):
    solution = Solution()
    assert solution.lowestCommonAncestor(None, bst.left, bst.right) is None
    assert solution.lowestCommonAncestor(bst, None, bst.right) is None
    assert solution.lowestCommonAncestor(bst, bst.left, None) is None
