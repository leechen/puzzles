import unittest
from collections import deque
from graph_codec import GraphCodec, GraphNode

class TestGraphCodec(unittest.TestCase):
    def setUp(self):
        self.codec = GraphCodec()

    def assert_graphs_equal(self, g1: GraphNode | None, g2: GraphNode | None):
        """
        Helper method to verify two cyclic graphs are topologically 
        and structurally identical without infinite loops.
        """
        if g1 is None and g2 is None:
            return
        assert g1 is not None, "Expected non-None node, got None"
        assert g2 is not None, "Expected None, got non-None node"

        visited1: dict[int, GraphNode] = {}
        visited2: dict[int, GraphNode] = {}

        q1: deque[GraphNode] = deque([g1])
        q2: deque[GraphNode] = deque([g2])

        visited1[g1.val] = g1
        visited2[g2.val] = g2

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            self.assertEqual(n1.val, n2.val, f"Node value mismatch: {n1.val} vs {n2.val}")
            self.assertEqual(
                len(n1.neighbors), len(n2.neighbors),
                f"Neighbor counts mismatch for node {n1.val}"
            )

            for neighbor1, neighbor2 in zip(n1.neighbors, n2.neighbors):
                self.assertEqual(neighbor1.val, neighbor2.val)

                if neighbor1.val not in visited1:
                    visited1[neighbor1.val] = neighbor1
                    q1.append(neighbor1)

                if neighbor2.val not in visited2:
                    visited2[neighbor2.val] = neighbor2
                    q2.append(neighbor2)

        self.assertEqual(len(q1), len(q2), "Traversal queue states are out of sync")

    def test_empty_graph(self):
        """Test serializing/deserializing None."""
        root = None
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "")
        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node_no_neighbors(self):
        """Test a lone isolated node."""
        root = GraphNode(10)
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "10:")
        deserialized = self.codec.deserialize(serialized)
        self.assert_graphs_equal(root, deserialized)

    def test_single_node_self_loop(self):
        """Test a single node that points to itself (1 -> 1)."""
        root = GraphNode(1)
        root.neighbors.append(root)

        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1:1")
        deserialized = self.codec.deserialize(serialized)
        
        self.assert_graphs_equal(root, deserialized)
        assert deserialized is not None
        # Assert object reference identity for loop integrity
        self.assertIs(deserialized.neighbors[0], deserialized)

    def test_standard_cyclic_graph(self):
        """
        Test a 3-node cyclic directed graph:
        1 -> [2, 3]
        2 -> [3]
        3 -> [1]
        """
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)

        n1.neighbors = [n2, n3]
        n2.neighbors = [n3]
        n3.neighbors = [n1]

        serialized = self.codec.serialize(n1)
        deserialized = self.codec.deserialize(serialized)
        
        self.assert_graphs_equal(n1, deserialized)
        
        # Verify cycle pointer back to root preserves object identity
        assert deserialized is not None
        node3 = deserialized.neighbors[1]
        self.assertIs(node3.neighbors[0], deserialized)

    def test_bidirectional_two_node_cycle(self):
        """Test a mutual loop: 1 <-> 2"""
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n1.neighbors.append(n2)
        n2.neighbors.append(n1)

        serialized = self.codec.serialize(n1)
        deserialized = self.codec.deserialize(serialized)
        self.assert_graphs_equal(n1, deserialized)

    def test_negative_values(self):
        """Test graph with negative IDs and zero: -5 -> 0 -> -10 -> -5"""
        n_neg5 = GraphNode(-5)
        n_zero = GraphNode(0)
        n_neg10 = GraphNode(-10)

        n_neg5.neighbors.append(n_zero)
        n_zero.neighbors.append(n_neg10)
        n_neg10.neighbors.append(n_neg5)

        serialized = self.codec.serialize(n_neg5)
        deserialized = self.codec.deserialize(serialized)
        self.assert_graphs_equal(n_neg5, deserialized)


if __name__ == "__main__":
    unittest.main()