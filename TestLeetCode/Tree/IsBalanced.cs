public class IsBalancedSolutionWithValueTuple {
    public bool IsBalanced(TreeNode root) {
        return DFS(root).IsBalanced;
    }

    private (bool IsBalanced, int Height) DFS(TreeNode root) {
        if (root == null) {
            return (true, 0);
        }

        var left = DFS(root.left);
        var right = DFS(root.right);
        bool isBalanced = left.IsBalanced && right.IsBalanced && Math.Abs(left.Height - right.Height) <= 1;

        return (isBalanced, 1 + Math.Max(left.Height, right.Height));
    }
}

public class IsBalancedSolution {
    public bool IsBalanced(TreeNode root) {
        return DFS(root).IsBalanced;
    }

    private BalanceStatus DFS(TreeNode root) {
        if (root == null) {
            return new BalanceStatus(true, 0);
        }

        BalanceStatus left = DFS(root.left);
        BalanceStatus right = DFS(root.right);
        bool balanced = left.IsBalanced && right.IsBalanced && Math.Abs(left.Height - right.Height) <= 1;

        return new BalanceStatus(balanced, 1 + Math.Max(left.Height, right.Height));
    }
}

public class BalanceStatus {
    public bool IsBalanced { get; }
    public int Height { get; }

    public BalanceStatus(bool isBalanced, int height) {
        IsBalanced = isBalanced;
        Height = height;
    }
}
