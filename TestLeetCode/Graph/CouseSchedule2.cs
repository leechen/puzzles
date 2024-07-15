// https://leetcode.com/problems/course-schedule-ii/description/

public class FindOrderSolution {
    public int[] FindOrder(int numCourses, int[][] prerequisites) {
        // Step 1: build dependency map
        var reqMap = new Dictionary<int, IList<int>>();
        for (int i = 0; i < numCourses; i++) {
            reqMap[i] = new List<int>();
        }

        foreach (var prereq in prerequisites) {
            var cur = prereq[0];
            var pre = prereq[1];
            reqMap[pre].Add(cur);
        }

        var visited = new int[numCourses];
        var res = new List<int>();

        bool hasCycle(int course) {
            if (visited[course] == 1) { // visiting
                return true;
            }
            if (visited[course] == 2) { // visited
                return false;
            }

            visited[course] = 1;
            foreach (var dep in reqMap[course]) {
                if (hasCycle(dep)) { return true; }
            }
            visited[course] = 2;
            res.Add(course);
            return false;
        }

        // Step 2: go over all nodes and check for loops.
        // If no loop, add to res list.
        for (int course = 0; course < numCourses; course++) {
            if (visited[course] == 0 && hasCycle(course)) {
                return new int[0];
            }
        }
        
        res.Reverse();
        return res.ToArray();
    }
}
