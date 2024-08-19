// https://leetcode.com/problems/generate-parentheses/description/
// can be viewed as backtrack or stack but it is essentially DFS

using System.Text;

public class GenerateParenthesisSolution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        var seq = new StringBuilder();
        
        void Dfs(int open, int close) {
            if(seq.Length == n * 2) {
                // make a copy of seq by calling ToString()
                result.Add(seq.ToString());
                return;
            } 
            
            if(open < n) {
                seq.Append("(");
                Dfs(open + 1, close);
                // remove the last "("
                seq.Length -= 1;
            }
            // there is no else clause here since we want to explore both branches
            if(close < open) {
                seq.Append(")");
                Dfs(open, close + 1);
                // remove the last ")"
                seq.Length -= 1;
            }            
        }

        Dfs(0, 0);

        return result;
    }
}