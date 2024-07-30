// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
/*
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they 
add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 
1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
*/

public class TwoSumSolution {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0, r = numbers.Length - 1;

        while (l < r) {
            int curSum = numbers[l] + numbers[r];

            if (curSum > target) {
                r--;
            } else if (curSum < target) {
                l++;
            } else {
                // given a 1-indexed array in the question
                // notice C# can return an array like this.
                return [l + 1, r + 1];
            }
        }

        return [];  // This line should not be reached if the input guarantees a solution.
    }
}
