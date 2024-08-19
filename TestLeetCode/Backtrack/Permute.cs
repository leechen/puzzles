// 
// https://leetcode.com/problems/permutations/
// https://www.youtube.com/watch?v=FZe0UqISmUw&t=717s

public class PermuteSolution
{
    public IList<IList<int>> Permute(int[] nums)
    {
        // start with a new empty list so that we can add the first item
        var perms = new List<IList<int>> { new List<int>() };

        foreach (var n in nums)
        {
            var newPerms = new List<IList<int>>();
            // This is not a backtrack solution.
            // It is a iterative solution by inserting into all possible positions
            foreach (var p in perms)
            {
                for (int i = 0; i <= p.Count; i++)
                {
                    var pCopy = new List<int>(p);
                    pCopy.Insert(i, n);
                    newPerms.Add(pCopy);
                }
            }
            perms = newPerms;
        }

        return perms;
    }

   public IList<IList<int>> Permute2(int[] nums)
    {
        var result = new List<IList<int>>();
        PermuteRecursive(nums, 0, result);
        return result;
    }

    private void PermuteRecursive(int[] nums, int start, IList<IList<int>> result)
    {
        // Base case: when start index reaches the end, we have a complete permutation
        if (start == nums.Length)
        {
            result.Add(new List<int>(nums)); // Add a copy of the permutation to the result list
            return;
        }

        // Recursively swap and generate permutations
        for (int i = start; i < nums.Length; i++)
        {
            // Swap the current element with the start element
            Swap(nums, i, start);

            // Recurse with the next element as the start
            PermuteRecursive(nums, start + 1, result);

            // Backtrack (undo the swap)
            Swap(nums, i, start);
        }
    }

    // Helper function to swap two elements in an array
    private void Swap(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

}
