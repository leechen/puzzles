// https://leetcode.com/problems/jump-game/description/
// You are given an integer array nums. You are initially positioned at the array's first index, 
// and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

public class CanJumpSolution {
    public bool CanJump(int[] nums) {
        int len = nums.Length;
        int goal = len-1;
        for (int i=len-1; i>=0; i--)
        {
            if (i + nums[i] >= goal)
            {
                goal = i;
            }
        }
        return goal == 0;
    }
}