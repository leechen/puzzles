// 
// https://leetcode.com/problems/permutations/
// https://www.youtube.com/watch?v=FZe0UqISmUw&t=717s

public class PermuteSolution {
    public IList<IList<int>> Permute(int[] nums) {
        // start with a new empty list so that we can add the first item
        var perms = new List<IList<int>> { new List<int>() };
        
        foreach (var n in nums) {
            var newPerms = new List<IList<int>>();
            foreach (var p in perms) {
                for (int i = 0; i <= p.Count; i++) {
                    var pCopy = new List<int>(p);
                    pCopy.Insert(i, n);
                    newPerms.Add(pCopy);
                }
            }
            perms = newPerms;
        }
        
        return perms;
    }
}
