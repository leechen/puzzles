public class SubsetsSolution {
    private List<int> subset = new List<int>();
    private List<IList<int>> result = new List<IList<int>>();        
        
    public IList<IList<int>> Subsets(int[] nums) {
        backtrack(0, nums);
        return result;  
    }

    private void backtrack(int i, int[] nums) {
        if(i >= nums.Length) {
            result.Add(new List<int>(subset));
            return;
        }

        subset.Add(nums[i]);
        backtrack(i + 1, nums);
        // Two branches to explore, after the first adding the number, remove it to 
        // explore the other path (without that number)
        subset.Remove(nums[i]);
        backtrack(i + 1, nums);           
    }
}