/**************************************************************
https://leetcode.com/problems/product-of-array-except-self/description/
https://www.youtube.com/watch?v=bNvIQI2wAjk
**************************************************************/
public class ProductExceptSelfSolution {
    public int[] ProductExceptSelf(int[] nums) {
            int len = nums.Length;
            int[] res = new int[len];
            res[0] = 1;

            for (int i = 1; i < len; i++)
            {
                res[i] = res[i - 1] * nums[i - 1];
            }

            int right = 1;
            for (int i = len - 1; i >= 0; i--)
            {
                res[i] *= right;
                right *= nums[i];
            }

            return res;        
    }
}
