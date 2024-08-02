public class LowestCommonAncestorBstSolution {
    public TreeNode LowestCommonAncestorIter(TreeNode root, TreeNode p, TreeNode q) {
        while (true) {
            if (root.val < p.val && root.val < q.val) {
                root = root.right;
            } else if (root.val > p.val && root.val > q.val) {
                root = root.left;
            } else {
                return root;
            }
        }
    }

    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Traverse Right child
        if (p.val > root.val && q.val > root.val) {
            return LowestCommonAncestor(root.right, p, q);
        }
        
        // Traverse Left Child
        if (p.val < root.val && q.val < root.val) {
            return LowestCommonAncestor(root.left, p, q);
        }
        
        return root;
    }
}
