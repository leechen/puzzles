// https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
//
// A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
// A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
// The path sum of a path is the sum of the node's values in the path.
// Given the root of a binary tree, return the maximum path sum of any non-empty path.

public class MaxPathSumSolution {
    private int maxSum;

    public int MaxPathSum(TreeNode root) {
        maxSum = int.MinValue;
        MaxGain(root);
        return maxSum;
    }

    // The tricky point is that we need return/update two values:
    // 1. maxSum
    // 2. maxGain
    // So here we use a class member variable to store one and return the maxGain only
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