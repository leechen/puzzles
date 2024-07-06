/** https://leetcode.com/problems/binary-tree-level-order-traversal/
 *
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
public class LevelOrderSolution {
    public IList<IList<int>> LevelOrder(TreeNode root) {

        var res = new List<IList<int>>();
        if (root == null) return res;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Any()) {
            var level = new List<int>();
            int len = queue.Count;

            for (int i=0; i<len; i++) {
                var curNode = queue.Dequeue();
                level.Add(curNode.val);

                if (curNode.left != null) {
                    queue.Enqueue(curNode.left);
                }
                if (curNode.right != null) {
                    queue.Enqueue(curNode.right);
                }                
            }
            res.Add(level);
        }
        
        return res;
    }
}