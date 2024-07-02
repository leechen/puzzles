public class Solution
{
    public int[][] Merge(int[][] intervals)
    {
        if (intervals.Length == 0) return new int[0][];

        intervals = intervals.OrderBy(x => x[0]).ToArray();
        List<int[]> res = new List<int[]> { intervals[0] };

        foreach (var interval in intervals.Skip(1))
        {
            int lastEnd = res[res.Count - 1][1];
            int start = interval[0];
            int end = interval[1];

            if (lastEnd >= start)
            {
                res[res.Count - 1][1] = Math.Max(lastEnd, end);
            }
            else
            {
                res.Add(new int[] { start, end });
            }
        }

        return res.ToArray();
    }
}