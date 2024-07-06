public class SearchSolution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length - 1;

        while (l <= r) {
            int m = l + ((r - l) / 2);  // (l + r) / 2 can lead to overflow
            if (nums[m] > target) {
                r = m - 1;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                return m;
            }
        }

        return -1;
    }
}
