// https://leetcode.com/problems/group-anagrams/description

// 49. Group Anagrams

// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
// typically using all the original letters exactly once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

public class GroupAnagramsSolution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var ans = new Dictionary<string, List<string>>();

        foreach (var s in strs) {
            var count = new int[26];
            /*************************************************************************************
                One way is to sort the words and use the sorted words as keys, that is O(NlogN)
                A optimization is to use concatenated count of each char as keys, this is O(N)
            /*************************************************************************************/
            foreach (var c in s) {
                count[c - 'a']++;
            }
            var key = string.Join(",", count);
            if (!ans.ContainsKey(key)) {
                ans[key] = new List<string>();
            }
            ans[key].Add(s);
        }

        return ans.Values.ToList<IList<string>>();
    }
}
