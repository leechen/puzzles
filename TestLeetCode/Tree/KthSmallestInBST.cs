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

    public int KthSmallestIter(TreeNode root, int k) {
        var stack = new Stack<TreeNode>();
        var current = root;
        int count = 0;

        while (current != null || stack.Count > 0) {
            // Go to the leftmost node
            while (current != null) {
                stack.Push(current);
                current = current.left;
            }
            
            // Visit the node
            current = stack.Pop();
            count++;
            
            // If we've visited k nodes, return the value of the current node
            if (count == k) {
                return current.val;
            }
            
            // Go to the right node
            current = current.right;
        }
        
        return -1; // This return statement should never be reached if k is valid
    }
}