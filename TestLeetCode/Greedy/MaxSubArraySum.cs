// https://leetcode.com/problems/maximum-subarray/description/
/* Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
*/
public class MaxSubArraySolution {
    public int MaxSubArray(int[] array) {
            if (array == null || array.Length == 0) return Int32.MinValue;
            int curMax = array[0];

            int curSum = 0;
            foreach (int x in array)
            {
                curSum += x;
                if (curSum > curMax) curMax = curSum;
                if (curSum < 0) curSum = 0;
            }

            return curMax;        
    }
}