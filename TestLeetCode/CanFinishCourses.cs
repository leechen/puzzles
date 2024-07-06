namespace TestLeetCode;

public class CanFinishCoursesSolution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        // Step 1: build dependency map
        // 
        var reqMap = new Dictionary<int, IList<int>>();
        foreach (var prereq in prerequisites)
        {
            var cur =prereq[0];
            if (reqMap.ContainsKey(cur))
            {
                reqMap[cur].Add(prereq[1]);
            }
            else
            {
                var val = new List<int>
                {
                    prereq[1]
                };
                reqMap.Add(cur, val);
            }
        }
        
        var visited = new HashSet<int>();
        var canComplete = new HashSet<int>();

        // Step 2: go over all node and check for loops.
        // If no loop, add to canComplete set.
        // Else, just return false.
        for (int course=0; course<numCourses; course++)
        {
            if (hasCycle(course, reqMap, visited, canComplete))
            {
                return false;
            }
            else
            {
                canComplete.Add(course);
            }
        }
        return true;
    }

    bool hasCycle(int course, Dictionary<int, IList<int>> dependencyMap, HashSet<int> visited, HashSet<int> canComplete)
    {
        if (canComplete.Contains(course)) { return false; } 
        // if we visit a visited node again, then loop exist
        if (visited.Contains(course)) { return true; }

        visited.Add(course);

        if (dependencyMap.ContainsKey(course))
        {
            foreach(var dep in dependencyMap[course])
            {
                if (hasCycle(dep, dependencyMap, visited, canComplete)) { return true; }
            }
        }
        visited.Remove(course);
        return false;
    }
}