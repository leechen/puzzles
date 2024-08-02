// https://leetcode.com/problems/invert-binary-tree/

public class InvertTreeSolution {
    public TreeNode InvertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        // Swap the children
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        // Make 2 recursive calls
        InvertTree(root.left);
        InvertTree(root.right);

        return root;
    }
}