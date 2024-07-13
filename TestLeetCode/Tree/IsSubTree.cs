public class IsSubtreeSolution {
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null) return true;
        if (root == null) return false;

        if (IsSameTree(root, subRoot)) {
            return true;
        }
        return  IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
    }

    bool IsSameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;

        if (root == null || subRoot == null) return false;
        if (root.val != subRoot.val) return false;

        return IsSameTree(root.left, subRoot.left) && IsSameTree(root.right, subRoot.right);
    }
}