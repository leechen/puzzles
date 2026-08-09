class ValidTree:
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if n == 0: return True
        if len(edges) != n - 1: return False
        graph = [[] for _ in range(n)]
        for left, right in edges: graph[left].append(right); graph[right].append(left)
        seen = set()
        def visit(node: int, parent: int) -> None:
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in seen: visit(neighbor, node)
        visit(0, -1)
        return len(seen) == n
