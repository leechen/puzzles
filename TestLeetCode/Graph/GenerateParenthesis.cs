// https://leetcode.com/problems/generate-parentheses/description/
// can be viewed as backtrack or stack but it is essentially DFS

public class GenerateParenthesisSolution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        var seq = new StringBuilder();
        
        void Dfs(int open, int close) {
            if(seq.Length == n * 2) {
                result.Add(seq.ToString());
                return;
            } 
            
            if(open < n) {
                seq.Append("(");
                Dfs(open + 1, close);
                seq.Length -= 1;
            }
            if(close < open) {
                seq.Append(")");
                Dfs(open, close + 1);
                seq.Length -= 1;
            }
            
        }

        Dfs(0, 0);

        return result;
    }
}