class GraphNode:
    def __init__(self, val: int = 0, neighbors: list['GraphNode'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class GraphCodec:
    def serialize(self, node: GraphNode | None) -> str:
        """Encodes a directed graph to an adjacency list string."""
        if not node:
            return ""

        # Use a dict/list to guarantee insertion order
        visited: dict[GraphNode, bool] = {}
        ordered_nodes: list[GraphNode] = []

        def dfs(curr: GraphNode) -> None:
            visited[curr] = True
            ordered_nodes.append(curr)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(node)

        # Build entries in the deterministic order they were visited
        adj_records: list[str] = []
        for curr in ordered_nodes:
            neighbor_ids = ",".join(str(nbr.val) for nbr in curr.neighbors)
            adj_records.append(f"{curr.val}:{neighbor_ids}")

        return "|".join(adj_records)

    def deserialize(self, data: str) -> GraphNode | None:
        """Decodes the serialized string back to the graph structure."""
        if not data:
            return None

        node_map: dict[int, GraphNode] = {}
        entries = data.split("|")

        # Pass 1: Instantiate nodes
        for entry in entries:
            val_str, _ = entry.split(":")
            val = int(val_str)
            if val not in node_map:
                node_map[val] = GraphNode(val)

        # Pass 2: Connect neighbor pointers
        for entry in entries:
            val_str, neighbors_str = entry.split(":")
            curr_node = node_map[int(val_str)]
            
            if neighbors_str:
                for nbr_str in neighbors_str.split(","):
                    nbr_val = int(nbr_str)
                    curr_node.neighbors.append(node_map[nbr_val])

        # entries[0] is guaranteed to be the original root node
        first_val = int(entries[0].split(":")[0])
        return node_map[first_val]