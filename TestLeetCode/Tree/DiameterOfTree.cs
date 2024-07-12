public class DiameterOfBinaryTreeSolution {
    private int res = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        DFS(root);
        return res;
    }

    private int DFS(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = DFS(node.left);
        int right = DFS(node.right);
        res = Math.Max(res, left + right);

        return 1 + Math.Max(left, right);
    }
}