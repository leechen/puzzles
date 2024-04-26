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

public class Cordinate : IEqualityComparer<Cordinate> {
    public Cordinate(int x, int y) {
        X = x;
        Y= y;
    }
    public int X;
    public int Y;

    public bool Equals(Cordinate? x, Cordinate? y)
    {
        return x?.X == y?.X && y?.Y == y?.Y;
    }

    public int GetHashCode([DisallowNull] Cordinate obj)
    {
        return obj.X * 263 + obj.Y;
    }
}

class MazeSolution
{
    public bool HasPath(int[,] maze, out IList<Cordinate> path) {
        var visited = new HashSet<Cordinate>();
        var start = new Cordinate(0, 0);
        var len = maze.GetLength(0);
        var wid = maze.GetLength(1);

        var end = new Cordinate(len, wid);
        path = new List<Cordinate>();


        bool Helper(Cordinate cur, IList<Cordinate> path) {
            if (visited.Contains(cur)) { return false; }

            visited.Add(cur); //0,0, 1,0

            if (cur == end) { // 6,6
                path.Add(cur);
                return true;
            }

            var x = cur.X;
            var y = cur.Y;
            if (maze[x,y] == 1) {
                return false;
            }

            if (x+1 < len && Helper(new Cordinate(x+1, y), path)) {
                path.Add(cur);
                return true;
            }
            if (x-1 > 0 && Helper(new Cordinate(x-1, y), path)) {
                path.Add(cur);
                return true;
            }  
            if (y+1 < wid && Helper(new Cordinate(x, y+1), path)) {
                path.Add(cur);
                return true;
            } 
            if (y-1 > 0 && Helper(new Cordinate(x, y-1), path)) {
                path.Add(cur);
                return true;                
            }
            return false;
        }

        Helper(start, path);

        return path.Any();
    }
}


// Your previous Plain Text content is preserved below:

// Welcome to Meta!

// This is just a simple shared plaintext pad, with no execution capabilities.

// When you know what language you would like to use for your interview,
// simply choose it from the dropdown in the left bar.

// Enjoy your interview!