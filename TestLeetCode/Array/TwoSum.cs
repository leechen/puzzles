// https://leetcode.com/problems/two-sum/description/

  namespace TestLeetCode;
  public class TwoSumSolution{

   public static int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> indices = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            var diff = target - nums[i];
            if (indices.ContainsKey(diff)) {
                return new int[] {indices[diff], i};
            }
            indices[nums[i]] = i;
        }
        return null;
    }
}