using System.Text;

public class IsPalindromeSolution {
    public bool IsPalindrome(string s) {
        var sb = new StringBuilder();
        foreach (var ch in s) {
            if (Char.IsLetterOrDigit(ch)) {
                sb.Append(Char.ToLower(ch));
            }
        }

        var len = sb.Length;

        for (int i = 0; i<len/2; i++) {
            if (sb[i] != sb[len-1-i]) {
                return false;
            }
        }

        return true;
    }
}