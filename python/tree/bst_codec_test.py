import unittest
from python.tree.bst_codec import BSTCodec
from python.common import TreeNode  # Or from python.tree.bst_codec import TreeNode

class TestBSTCodec(unittest.TestCase):
    def setUp(self):
        self.codec = BSTCodec()

    def assert_trees_equal(self, t1: TreeNode | None, t2: TreeNode | None):
        """Recursively checks if two BSTs are structurally identical with equal values."""
        if t1 is None and t2 is None:
            return
        
        # Native assertions serve as type guards for static analyzers
        assert t1 is not None, "Expected non-None node, got None"
        assert t2 is not None, "Expected None, got non-None node"

        self.assertEqual(t1.val, t2.val, f"Value mismatch: {t1.val} != {t2.val}")
        self.assert_trees_equal(t1.left, t2.left)
        self.assert_trees_equal(t1.right, t2.right)

    def test_empty_tree(self):
        """Test null/empty BST."""
        root = None
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "")
        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node(self):
        """Test a BST with a single node."""
        root = TreeNode(42)
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "42")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_balanced_bst(self):
        r"""
        Test a standard balanced BST:
               5
             f/   \
            3     8
           / \   / \
          2   4 6   9
        """
        root = TreeNode(5,
            TreeNode(3, TreeNode(2), TreeNode(4)),
            TreeNode(8, TreeNode(6), TreeNode(9))
        )
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "5 3 2 4 8 6 9")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_left_skewed_bst(self):
        """
        Test a strictly left-skewed BST (descending chain):
            5 -> 4 -> 3 -> 2 -> 1
        """
        root = TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "5 4 3 2 1")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_right_skewed_bst(self):
        """
        Test a strictly right-skewed BST (ascending chain):
            1 -> 2 -> 3 -> 4 -> 5
        """
        root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5)))))
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1 2 3 4 5")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_negative_values(self):
        """
        Test a BST containing negative values and zero:
               0
             /   \
           -10    10
             \
             -5
        """
        root = TreeNode(0,
            TreeNode(-10, right=TreeNode(-5)),
            TreeNode(10)
        )
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "0 -10 -5 10")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_zigzag_bst(self):
        """
        Test a zigzag BST:
             10
            /
           5
            \
             7
        """
        root = TreeNode(10, TreeNode(5, right=TreeNode(7)))
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "10 5 7")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)


if __name__ == "__main__":
    unittest.main()