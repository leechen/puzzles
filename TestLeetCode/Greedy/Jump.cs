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