from collections import deque

class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        neighbor_vals = [n.val for n in self.neighbors]
        return f"Node(val={self.val}, neighbors={neighbor_vals})"
    
class GraphCodec:
    def serialize(self, node: 'Node | None') -> str:
        """Serializes a directed/undirected graph to a string using BFS adjacency list."""
        if not node:
            return ""

        # Map each unique node object (by id or value) to a visited set
        # Assuming node.val is unique; if not, use id(node) as key
        visited: set[Node] = set([node])
        queue: deque[Node] = deque([node])
        records: list[str] = []

        while queue:
            curr = queue.popleft()
            neighbor_vals = []
            for neighbor in curr.neighbors:
                neighbor_vals.append(str(neighbor.val))
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            records.append(f"{curr.val}:{','.join(neighbor_vals)}")

        return "#".join(records)

    def deserialize(self, data: str) -> 'Node | None':
        """Deserializes the string representation back to the connected graph."""
        if not data:
            return None

        # Pass 1: Instantiate all Node objects and store them in a lookup map
        nodes: dict[int, Node] = {}
        adjacency_data: list[tuple[int, list[int]]] = []

        for record in data.split("#"):
            if not record:
                continue
            val_str, _, neighbors_str = record.partition(":")
            node_val = int(val_str)

            if node_val not in nodes:
                nodes[node_val] = Node(node_val)

            neighbor_vals = [int(v) for v in neighbors_str.split(",") if v]
            adjacency_data.append((node_val, neighbor_vals))

        # Ensure any neighbor that was never a root record is also created
        for _, neighbor_vals in adjacency_data:
            for n_val in neighbor_vals:
                if n_val not in nodes:
                    nodes[n_val] = Node(n_val)

        # Pass 2: Connect neighbor pointers
        for node_val, neighbor_vals in adjacency_data:
            nodes[node_val].neighbors = [nodes[n_val] for n_val in neighbor_vals]

        # Return the starting node (first record in adjacency_data)
        start_val = adjacency_data[0][0]
        return nodes[start_val]