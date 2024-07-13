public class LowestCommonAncestorSolution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        if (root == null) { return null; }
        if (root == p || root == q) { return root; }
        
        var left = LowestCommonAncestor(root.left, p, q);
        var right = LowestCommonAncestor(root.right, p, q);
        if (left != null && right != null)
        {
            return root;
        }
        
        return left == null ? right : left;
    }
}