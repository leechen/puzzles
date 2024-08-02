

public class LetterCombinationsSolution {
    public IList<string> LetterCombinations(string digits) {
        var res = new List<string>();
        var digitToChar = new Dictionary<char, string> {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        void Helper(int i, string curStr) {
            if (curStr.Length == digits.Length) {
                res.Add(curStr);
                return;
            }
            foreach (char c in digitToChar[digits[i]]) {
                // The reason we don't need to remove or reduce i is that these are passed in by value
                Helper(i + 1, curStr + c);
            }
        }

        if (!string.IsNullOrEmpty(digits)) {
            Helper(0, "");
        }

        return res;
    }
}
