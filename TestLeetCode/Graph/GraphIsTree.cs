public class ValidTreeSolution {
    public bool ValidTree(int n, int[][] edges) {
        if (n == 0) {
            return true;
        }

        // Step 1: Create adjacency list
        var adj = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }
        
        foreach (var edge in edges) {
            int n1 = edge[0], n2 = edge[1];
            adj[n1].Add(n2);
            adj[n2].Add(n1);
        }

        var visit = new HashSet<int>();

        // Step 2: Depth-First Search (DFS) to check for cycles and connectivity
        bool Dfs(int node, int parent) {
            if (visit.Contains(node)) {
                return false;
            }

            visit.Add(node);
            foreach (var neighbor in adj[node]) {
                if (neighbor == parent) {
                    continue;
                }
                if (!Dfs(neighbor, node)) {
                    return false;
                }
            }
            return true;
        }

        // Check if the graph is connected and acyclic
        return Dfs(0, -1) && visit.Count == n;
    }
}
