namespace TestLeetCode;

public class CanFinishCoursesSolution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
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
        var cleared = new HashSet<int>();

        for (int i=0; i<numCourses; i++)
        {
            if (hasCycle(i, reqMap, visited, cleared))
            {
                return false;
            }
            else
            {
                cleared.Add(i);
            }
        }
        return true;
    }

    bool hasCycle(int course, Dictionary<int, IList<int>> map, HashSet<int> visited, HashSet<int> cleared)
    {
        if (cleared.Contains(course)) { return false; } 
        if (visited.Contains(course)) { return true; }

        visited.Add(course);

        if (map.ContainsKey(course))
        {
            foreach(var dep in map[course])
            {
                if (hasCycle(dep, map, visited, cleared)) { return true; }
            }
        }
        visited.Remove(course);
        return false;
    }
}