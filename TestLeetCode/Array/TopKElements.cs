/**************************************************************
https://leetcode.com/problems/top-k-frequent-elements/description/
https://www.youtube.com/watch?v=YPTqKIgVk-k

hint: bucket
**************************************************************/

public class TopKFrequentSolution
{
    public IList<int> TopKFrequent(int[] nums, int k)
    {
        int length = nums.Length;
        List<int>[] freq = new List<int>[length + 1];
        for (int i = 0; i < freq.Length; i++)
        {
            freq[i] = new List<int>();
        }

        Dictionary<int, int> counts = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (counts.ContainsKey(num))
            {
                counts[num]++;
            }
            else
            {
                counts[num] = 1;
            }
        }

        foreach (var entry in counts)
        {
            freq[entry.Value].Add(entry.Key);
        }

        List<int> res = new List<int>();
        // Count is natually sorted already, so going from 
        // highest count to lowest
        for (int i = length; i > 0; i--)
        {
            foreach (int num in freq[i])
            {
                res.Add(num);
                if (res.Count == k)
                {
                    return res;
                }
            }
        }

        return res;
    }
}

