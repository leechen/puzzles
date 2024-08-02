// https://leetcode.com/problems/diameter-of-binary-tree/description/
// https://www.youtube.com/watch?v=K81C31ytOZE

public class DiameterOfBinaryTreeSolution {
    private int res = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        DFS(root);
        return res;
    }

    // Returns height instead of result; we need to calculate result in every 
    // call since root may not be part of the path in getting the diameter.
    private int DFS(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = DFS(node.left);
        int right = DFS(node.right);
        res = Math.Max(res, left + right);

        return 1 + Math.Max(left, right);
    }
}