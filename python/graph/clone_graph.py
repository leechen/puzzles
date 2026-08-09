class GraphNode:
    def __init__(self, value: int = 0, neighbors: list["GraphNode"] | None = None):
        self.val = value
        self.neighbors = neighbors or []


class CloneGraph:
    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        copies = {}
        def clone(current):
            if current is None: return None
            if current not in copies:
                copies[current] = GraphNode(current.val)
                copies[current].neighbors = [clone(neighbor) for neighbor in current.neighbors]
            return copies[current]
        return clone(node)
