// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Given a string s, find the length of the longest 
// substring
//  without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

public class LengthOfLongestSubstringSolution {
    public int LengthOfLongestSubstringV2(string s) {
        HashSet<char> charSet = new HashSet<char>();
        int left = 0;
        int res = 0;

        for (int right = 0; right < s.Length; right++) {
            while (charSet.Contains(s[right])) {
                charSet.Remove(s[left]);
                left++;
            }
            charSet.Add(s[right]);
            res = Math.Max(res, right - left + 1);
        }

        return res;
    }

    public int LengthOfLongestSubstring(string s) {
        if (String.IsNullOrEmpty(s)) { return 0; }

        int len = s.Length;
        int begin = 0;
        int max = 0;

        while (begin < len) {
            var existing = new HashSet<char>();

            existing.Add(s[begin]);
            int end = begin + 1;
            while (end < len && !existing.Contains(s[end])) {
                existing.Add(s[end]);
                end++;
            }

            max = Math.Max(max, end - begin);
            // This need to start from next instead of "end" because the beginning of the string
            // may be the same the end, and the substring is all unique except index at begin and end.
            begin++;
        }
        return max;
    }
}