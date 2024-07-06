/// <summary>
/// https://leetcode.com/problems/kth-smallest-element-in-a-bst/
/// </summary>
public class KthSmallestSolution {
    int count = 0;
    // Simply doing the in-order traversal
    public int KthSmallest(TreeNode root, int k)
    {
        if (root == null) return 0;
        int res = KthSmallest(root.left, k);
        if (count == k) { return res; }
        else {
            count++;
            if (count == k) { 
                return root.val;
            }
            return KthSmallest(root.right, k);
        }
    }
}