from python.lowestCommonAncestor import Solution


def test_recursive_lca_for_nodes_on_different_sides(bst):
    assert Solution().lowestCommonAncestor(bst, bst.left, bst.right) is bst


def test_recursive_lca_when_one_node_is_ancestor(bst):
    assert Solution().lowestCommonAncestor(bst, bst.left, bst.left.right) is bst.left


def test_iterative_lca_in_subtree(bst):
    assert Solution().lowestCommonAncestorIter(
        bst, bst.left.right.left, bst.left.right.right
    ) is bst.left.right


def test_lca_rejects_missing_inputs(bst):
    solution = Solution()
    assert solution.lowestCommonAncestor(None, bst.left, bst.right) is None
    assert solution.lowestCommonAncestor(bst, None, bst.right) is None
    assert solution.lowestCommonAncestor(bst, bst.left, None) is None
