  namespace TestLeetCode;
  public class TwoSumSolution{

   public static int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();

        var result = new int[2];
                
        for (int i=0; i<nums.Length; i++)
        {
            int key = target - nums[i];
            if (dict.ContainsKey(key))
            {
                result[0] = i;
                result[1] = dict[key];
            }
            
            if (!dict.ContainsKey(nums[i]))
            {
                dict.Add(nums[i], i);
            }
        }

        return result;
    }
} 