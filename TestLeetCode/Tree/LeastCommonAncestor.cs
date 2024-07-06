public class LowestCommonAncestorSolution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        }

        if (root.val == p.val || root.val == q.val) {
            return root;
        }
        
        // since p and q are NOT guranteed to be in order, so need to consider both conditions
        if ((root.val > p.val && root.val < q.val) 
            || (root.val < p.val && root.val > q.val)) {
                return root;
        }

        if (root.val > p.val && root.val > q.val) {
            return LowestCommonAncestor(root.left, p, q);
        }
        return  LowestCommonAncestor(root.right, p, q);
    }
}