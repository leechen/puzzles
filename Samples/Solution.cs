
public class Solution {
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
            dict.Add(nums[i], i);
        }

        return result;

    }

    public static void main()
    {
        var result = TwoSum(new int[]{2,7,11,15}, 9);
        Console.WriteLine(result.Length);
    }
}