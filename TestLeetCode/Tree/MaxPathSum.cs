public class MaxPathSumSolution {
    private int maxSum;

    public int MaxPathSum(TreeNode root) {
        maxSum = int.MinValue;
        MaxGain(root);
        return maxSum;
    }

    private int MaxGain(TreeNode node) {
        if (node == null) {
            return 0;
        }

        // Recursively get the maximum gain from the left and right subtrees
        int leftGain = Math.Max(MaxGain(node.left), 0);
        int rightGain = Math.Max(MaxGain(node.right), 0);

        // Calculate the sum of the current as the root (split)
        int currentPathSum = node.val + leftGain + rightGain;

        // Update maxSum if the current path is better
        maxSum = Math.Max(maxSum, currentPathSum);

        // Return the maximum gain the node and one of its subtrees can contribute
        return node.val + Math.Max(leftGain, rightGain);
    }
}