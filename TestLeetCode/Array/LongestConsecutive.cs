// https://leetcode.com/problems/longest-consecutive-sequence/description/
// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.

using System;
using System.Collections.Generic;

public class LongestConsecutiveSolution
{
    private bool IsStartOfSeq(int num, HashSet<int> numSet)
    {
        return !numSet.Contains(num - 1);
    }

    public int LongestConsecutive(int[] nums)
    {
        if (nums.Length == 0)
        {
            return 0;
        }

        int length = nums.Length;
        HashSet<int> numSet = new HashSet<int>(nums);
        int localMax = 1;
        int curMax = 1;

        foreach (int num in nums)
        {
            if (IsStartOfSeq(num, numSet))
            {
                int offset = 1;
                while (numSet.Contains(num + offset) && curMax < length)
                {
                    curMax++;
                    offset++;
                }
                localMax = Math.Max(localMax, curMax);
                curMax = 1;
            }
        }

        return localMax;
    }
}
