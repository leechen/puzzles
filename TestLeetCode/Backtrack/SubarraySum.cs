// https://leetcode.com/problems/combination-sum/description/
// https://www.youtube.com/watch?v=GBKI9VSKdGg

public class CombinationSumSolution {
    IList<IList<int>> result = new List<IList<int>>();
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        void backtrack(int index, List<int> path, int total) {
            if(total == target) {
                result.Add(path.ToList());
                return;
            }
        
            if(total > target || index >= candidates.Length) return;
            
            path.Add(candidates[index]);
            backtrack(index, 
                    path, 
                    total + candidates[index]
                    );
            
            path.Remove(path.Last());
            
            backtrack(index + 1, 
                    path, 
                    total
                    );
        }

        backtrack(0, new List<int>(), 0);
        return result;
    }
}
