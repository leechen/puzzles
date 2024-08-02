// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
// 

public class MaxDepthSolution
{
    public int MaxDepth(TreeNode root)
    {
        if (root == null) return 0;

        return 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
    }
}