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

        bool hasCycle(int course)
        {
            if (canComplete.Contains(course)) { return false; } 
            // if we visit a visited node again, then loop exist
            if (visited.Contains(course)) { return true; }

            visited.Add(course);

            if (reqMap.ContainsKey(course))
            {
                foreach(var dep in reqMap[course])
                {
                    if (hasCycle(dep)) { return true; }
                }
            }
            visited.Remove(course);
            return false;
        }

        // Step 2: go over all node and check for loops.
        // If no loop, add to canComplete set.
        // Else, just return false.
        // why go over all nodes? b/c nodes maybe disconnected and 
        // some sub-gruop may contains loop
        for (int course=0; course<numCourses; course++)
        {
            if (hasCycle(course))
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
}