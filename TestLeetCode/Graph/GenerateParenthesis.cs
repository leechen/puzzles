using System.Text;

public class GenerateParenthesisSolution {
    public IList<string> GenerateParenthesis(int n) {
        var res = new List<string>();
        var acc = new StringBuilder();
        int open = 0;
        int close = 0;
        
        dfs(open, close);

        return res;

        // Inner function can capture scope outside this function, very useful to 
        // make the code concise.
        void dfs(int open, int close) {
            if (open == n && close == n) {
                res.Add(acc.ToString());
                return;
            }

            if (open == n) {
                acc.Append(")");
                dfs(open, close+1);
                acc.Length--; // remove the last char
            }
            else if (open == close) {
                acc.Append("(");
                dfs(open+1, close);
                acc.Length--; 
            }
            else {
                acc.Append("(");
                dfs(open+1, close);
                acc.Length--;            
                    
                acc.Append(")");
                dfs(open, close+1);
                acc.Length--;  
            }
        }
    }
}