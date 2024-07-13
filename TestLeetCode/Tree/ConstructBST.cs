// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

public class BuildTreeSolution {
    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.Length == 0 || inorder.Length == 0) {
            return null;
        }
        return BuildTreeHelper(preorder, 0, preorder.Length - 1, inorder, 0, inorder.Length - 1);
    }

    private TreeNode BuildTreeHelper(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[preStart]);
        int mid = inStart;
        while (inorder[mid] != root.val) {
            mid++;
        }

        root.left = BuildTreeHelper(preorder, preStart + 1, preStart + (mid - inStart), inorder, inStart, mid - 1);
        root.right = BuildTreeHelper(preorder, preStart + (mid - inStart) + 1, preEnd, inorder, mid + 1, inEnd);
        
        return root;
    }
}