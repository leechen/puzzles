// https://neetcode.io/problems/string-encode-and-decode
// https://www.youtube.com/watch?v=B1k_sxOSgv8

public class Codec {

   public string encode(IList<string> strs) {
      return string.Concat(strs.SelectMany(s=>  $"{s.Length}#{s}"));
   }

   public IList<string> decode(string s) {
      var res = new List<string>();
    
      var i = 0;
      while (i < s.Length) {
         var j = i;
         while (s[j] != '#') {
            ++j;
         }

         int.TryParse(s.Substring(i, j-i), out var len);
         j++;
         res.Add(s.Substring(j, len));
         i = j + len;
      }

      return res;
   }
}