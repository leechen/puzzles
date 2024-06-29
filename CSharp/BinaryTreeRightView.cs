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
public class Solution {
    public IList<int> RightSideView(TreeNode root) {
        var res = new List<int>();
        if (root == null) { return res; }

        Helper(root, res, 0);
        return res;
    }

    private void Helper(TreeNode curr, IList<int> result, int currDepth) {
        if (curr == null) { return; }
        if (currDepth == result.Count)
        {
            result.Add(curr.val);
        }

        Helper(curr.right, result, currDepth + 1);
        Helper(curr.left, result, currDepth + 1);
    }
}