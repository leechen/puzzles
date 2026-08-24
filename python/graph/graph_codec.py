class GraphNode:
    def __init__(self, val: int = 0, neighbors: list['GraphNode'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class GraphCodec:
    def serialize(self, node: GraphNode | None) -> str:
        if not node:
            return ""

        # Using dict as an ordered set: preserves exact DFS discovery order
        visited: dict[GraphNode, None] = {}

        def dfs(curr: GraphNode) -> None:
            visited[curr] = None  # Inserts in discovery order with O(1) deduplication
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(node)

        # Build entries directly from visited keys
        adj_records = [
            f"{curr.val}:{','.join(str(nbr.val) for nbr in curr.neighbors)}"
            for curr in visited
        ]

        return "|".join(adj_records)

    def deserialize(self, data: str) -> GraphNode | None:
        if not data:
            return None

        node_map: dict[int, GraphNode] = {}
        entries = data.split("|")

        # Pass 1: Instantiate all GraphNode objects
        for entry in entries:
            val = int(entry.split(":")[0])
            if val not in node_map:
                node_map[val] = GraphNode(val)

        # Pass 2: Connect neighbors
        for entry in entries:
            val_str, neighbors_str = entry.split(":")
            curr_node = node_map[int(val_str)]
            if neighbors_str:
                curr_node.neighbors = [node_map[int(nbr)] for nbr in neighbors_str.split(",")]

        # First entry is guaranteed to be the root node
        return node_map[int(entries[0].split(":")[0])]