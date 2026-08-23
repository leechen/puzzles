import unittest
from codec import Node, Codec

class TestNaryTreeCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def assert_trees_equal(self, t1: Node | None, t2: Node | None):
        """Helper to recursively verify two N-ary trees are structurally identical."""
        if t1 is None and t2 is None:
            return
        
        # Type checkers understand built-in assert to eliminate None
        assert t1 is not None, "Expected non-None node, got None"
        assert t2 is not None, "Expected None, got non-None node"

        self.assertEqual(t1.val, t2.val, f"Values differ: {t1.val} vs {t2.val}")
        self.assertEqual(
            len(t1.children), len(t2.children), 
            f"Child counts differ for node {t1.val}"
        )
        for c1, c2 in zip(t1.children, t2.children):
            self.assert_trees_equal(c1, c2)

    def test_empty_tree(self):
        """Test null/empty tree."""
        root = None
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "")
        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node(self):
        """Test a tree with only a root node."""
        root = Node(42)
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "42,0")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_standard_multi_level_tree(self):
        """
        Test standard tree:
               1
            /  |  \
           3   2   4
          / \
         5   6
        """
        root = Node(1, [
            Node(3, [Node(5), Node(6)]),
            Node(2),
            Node(4)
        ])
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,3,3,2,5,0,6,0,2,0,4,0")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_negative_values_and_zeros(self):
        """Test nodes with negative numbers and zero values."""
        root = Node(0, [
            Node(-10, [Node(-25)]),
            Node(100)
        ])
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "0,2,-10,1,-25,0,100,0")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_skewed_deep_tree(self):
        """Test a singly linked (linear depth) N-ary tree."""
        # 1 -> 2 -> 3 -> 4
        root = Node(1, [Node(2, [Node(3, [Node(4)])])])
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,1,2,1,3,1,4,0")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)

    def test_wide_flat_tree(self):
        """Test a root node with many direct children (wide branching)."""
        root = Node(1, [Node(i) for i in range(2, 8)])
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,6,2,0,3,0,4,0,5,0,6,0,7,0")
        deserialized = self.codec.deserialize(serialized)
        self.assert_trees_equal(root, deserialized)


if __name__ == "__main__":
    unittest.main()