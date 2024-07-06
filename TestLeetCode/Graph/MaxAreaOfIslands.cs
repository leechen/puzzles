public class MaxAreaOfIslandSolution {
    public int MaxAreaOfIsland(int[][] grid) {
        if (grid == null || grid.Length == 0) { return 0; }
        if (grid[0].Length == 0) { return 0; }

        int length = grid.Length;
        int width = grid[0].Length;

        var visited = new bool[length][];
        for (int i = 0; i < length; i++) {
            visited[i] = new bool[width];
        }

        int max = 0;
        int cur = 0;

        for (int i = 0; i < length; i++) {
            for (int j = 0; j < width; j++) {
                if (!visited[i][j] && grid[i][j] == 1) {
                    cur = dfs(grid, visited, i, j);
                    max = Math.Max(max, cur);
                }
            }        
        }

        return max;
    }

    private int dfs(int[][] grid, bool[][] visited, int i, int j) {
        if (i < 0 || i >= grid.Length || j < 0 || j >= grid[0].Length ||
            visited[i][j] || grid[i][j] == 0) { return 0; }
        visited[i][j] = true;

        return 1 + dfs(grid, visited, i, j-1) + dfs(grid, visited, i, j+1)
            + dfs(grid, visited, i-1, j) + dfs(grid, visited, i+1, j);
    }
}
