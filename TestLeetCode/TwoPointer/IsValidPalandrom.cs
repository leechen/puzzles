// https://leetcode.com/problems/valid-palindrome/description/

using System.Text;

public class IsPalindromeSolution {
    public bool IsPalindrome(string s) {
        int left = 0;
        int right = s.Length - 1;

        while (left < right) {
            if (!char.IsLetterOrDigit(s[left])) {
                left++;
            } else if (!char.IsLetterOrDigit(s[right])) {
                right--;
            } else {
                if (char.ToLower(s[left]) != char.ToLower(s[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
}

public class IsPalindromeSolution2 {
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