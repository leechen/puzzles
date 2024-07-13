// Wrong approach:
public class IsValidBSTSolutionWrong {
    public bool IsValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        if (root.left != null && root.left.val >= root.val) { return false; }
        if (root.right != null && root.right.val <= root.val) { return false; }

        return IsValidBST(root.left) && IsValidBST(root.right);
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class IsValidBSTSolution {
    public bool IsValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        return IsValid(root.left, Int64.MinValue, root.val) && IsValid(root.right, root.val, Int64.MaxValue);
    }

    // Here we use long instead of int for max/min, because the corner case of Int32.MinValue and Int32.MaxValue as the 
    // possible tree node value
    private bool IsValid(TreeNode root, long min, long max) {
        if (root == null) { return true; }
        if (root.val <= min || root.val >= max) { return false; }

        return IsValid(root.left, min, Math.Min(root.val, max)) 
        && IsValid(root.right, Math.Max(root.val, min),  max);
    }
}