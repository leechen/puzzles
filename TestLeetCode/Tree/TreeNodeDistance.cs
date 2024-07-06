/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

namespace lintcode
{
    class Solution {
        /**
         * @param root: The root node of a binary tree.
         * @param p: The value of a node in the binary tree.
         * @param q: The value of a node in the binary tree.
         * @return: The distance between two nodes in a binary tree.
         */
        public int CalculateDistance(TreeNode root, int p, int q) {
            var lca = GetLCA(root, p, q);

            int distToP = CalDist(lca, p, 0);
            int distToQ = CalDist(lca, q, 0);
            return distToP + distToQ;
        }

        private int CalDist(TreeNode root, int p, int dist) {
            if (root == null) {
                return Int32.MaxValue;
            }
            if (root.val == p) {
                return dist;
            }

            return Math.Min(CalDist(root.left, p, dist+1), CalDist(root.right, p, dist+1));
        }

        /// Get least common acesstors
        private TreeNode GetLCA(TreeNode root, int p, int q) {
            if (root == null) {return null;}

            if (root.val == p || root.val == q) {
                return root;
            }
            var left = GetLCA(root.left, p, q);
            var right = GetLCA(root.right, p, q);

            if (left != null && right != null) {
                return root;
            }
            return left ?? right;
        }
    }
}