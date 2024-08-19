using System.Diagnostics.CodeAnalysis;

namespace TestLeetCode;

// To execute C#, please define "static void Main" on a class
// named Solution.

/**
 * Maze traversal problem
 * Input will be a 'maze' 
 * output will be two parts:
 * Is the maze passable? (true/false)
 * Return a path through the maze.
 * INput:
entrance -> 0 0 0 0 0 0 0
            0 0 1 0 0 1 0
            0 0 1 0 1 1 0
            0 0 1 0 1 0 1
            1 1 1 0 0 0 0 -> exit
 * Move up/down/left/right
entrance -> + + + + 0 0 0
            0 0 1 + 0 1 0
            0 0 1 + 1 1 0
            0 0 1 + 1 0 1
            1 1 1 + + + + -> exit
 */
class MazeSolution
{
    /**
        * @param maze: the maze
        * @param start: the start
        * @param destination: the destination
        * @return: whether the ball could stop at the destination
        */
    public bool HasPath(int[][] maze, int[] start, int[] destination) {
        if (maze == null || maze.Length == 0 || maze[0].Length == 0) { return false; }
        int rows = maze.Length;
        int cols = maze[0].Length;
        bool[][] visited = new bool[rows][];

        for (int i = 0; i < rows; i++)
        {
            visited[i] = new bool[cols];
        }

        bool HasPathHelper(int i, int j, int[] e) {                
            if (i < 0 || i >= rows) {return false;}
            if (j < 0 || j >= cols) { return false; }
            if (visited[i][j]) { return false; }
            visited[i][j] = true;
            if (i == e[0] && j == e[1]) { return true; }
            if (maze[i][j] == 1) { return false; }
            return HasPathHelper(i-1, j, e) || HasPathHelper(i+1, j, e) 
            || HasPathHelper(i, j-1, e) || HasPathHelper(i, j+1, e);
        }

        return HasPathHelper(start[0], start[1], destination);
    }
}



// Your previous Plain Text content is preserved below:

// Welcome to Meta!

// This is just a simple shared plaintext pad, with no execution capabilities.

// When you know what language you would like to use for your interview,
// simply choose it from the dropdown in the left bar.

// Enjoy your interview!