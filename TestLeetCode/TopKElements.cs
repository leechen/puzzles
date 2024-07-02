using System;
using System.Collections.Generic;
using System.Linq;


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
        foreach (int n in nums)
        {
            if (counts.ContainsKey(n))
            {
                counts[n]++;
            }
            else
            {
                counts[n] = 1;
            }
        }

        foreach (var entry in counts)
        {
            freq[entry.Value].Add(entry.Key);
        }

        List<int> res = new List<int>();
        for (int i = length; i > 0; i--)
        {
            foreach (int v in freq[i])
            {
                res.Add(v);
                if (res.Count == k)
                {
                    return res;
                }
            }
        }

        return res;
    }
}

