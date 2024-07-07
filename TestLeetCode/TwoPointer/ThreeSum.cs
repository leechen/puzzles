
public class ThreeSumSolution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        var res = new List<IList<int>>();
        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1, r = nums.Length - 1;
            while (l < r) {
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum > 0) {
                    r--;
                } else if (threeSum < 0) {
                    l++;
                } else {
                    res.Add([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    // skip duplicates
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        }

        return res;
    }

    public IList<IList<int>> ThreeSumOld(int[] nums) {
        Array.Sort(nums);

        var results = new List<IList<int>>();
        int len = nums.Length;
        if (len == 0) 
        {
            return results;
        }

        for (int i=0; i<len-2; i++)
        {
            if (i>1 && nums[i] == nums[i-1])
            {
                continue;
            }

            var twoSum = TwoSum(nums[1..], nums[i]);

            if ( twoSum[0] != twoSum[1])
            {
                var result = new List<int>();
                result.Add(nums[i]);
                result.Add(twoSum[0]);
                result.Add(twoSum[1]);
                results.Add(result);
            }
        }

        return results;
    }

    private int[] TwoSum(int[] ints, int v)
    {
        int left = 0;
        int right = ints.Length - 1;


        while (left < right)
        {
            int curValue = ints[left] + ints[right];

            if (curValue > -v)
            {
                right--;
            }
            else if (curValue < -v)
            {
                left++;
            }
            else
            {
                return [ints[left], ints[right]];
            }
        }

        return new int[2];
    }
}