// https://leetcode.com/problems/container-with-most-water/description/

public class MaxAreaSolution {
    public int MaxArea(int[] height) {
        int left = 0, right = height.Length - 1;
        int res = 0;

        while (left < right) {
            int l = height[left];
            int r = height[right];
            int cur = (right - left) * Math.Min(l, r);
            res = Math.Max(cur, res);
            if (l > r) {
                right--;
            } else {
                left++;
            }
        }

        return res;
    }
}
