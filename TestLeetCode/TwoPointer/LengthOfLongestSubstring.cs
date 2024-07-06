public class LengthOfLongestSubstringSolution {
    public int LengthOfLongestSubstringV2(string s) {
        HashSet<char> charSet = new HashSet<char>();
        int l = 0;
        int res = 0;

        for (int r = 0; r < s.Length; r++) {
            while (charSet.Contains(s[r])) {
                charSet.Remove(s[l]);
                l++;
            }
            charSet.Add(s[r]);
            res = Math.Max(res, r - l + 1);
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