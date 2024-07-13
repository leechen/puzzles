/**
 * https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/1310894435/
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
public class GoodNodesSolution {
    public int GoodNodes(TreeNode root) {
        // use DFS since it is more natural to find the good node (already visited all ancestors)
        if (root == null) { return 0; }

        int pathMax = root.val;
        return 1 + countGoodNodes(root.left, pathMax) + countGoodNodes(root.right, pathMax);
    }

    private int countGoodNodes(TreeNode root, int pathMax) {
        if (root == null) { return 0; }

        if (root.val >= pathMax) {
            return 1 + countGoodNodes(root.left, root.val) + countGoodNodes(root.right, root.val);
        }
        return countGoodNodes(root.left, pathMax) + countGoodNodes(root.right, pathMax);    
    }
}