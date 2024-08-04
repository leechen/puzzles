namespace TestLeetCode;

public class UnitTest1
{
    public int Add(int x) {
        if (x == 0) { return 0; }
        return x + Add(x-1);
    }

    [Fact]
    public void TestAdd()
    {
        var result = Add(5);
        Assert.True(result == 15);
    }
        

    [Fact]
    public void Test1()
    {
        var result = TwoSumSolution.TwoSum(new int[]{2,7,11,15}, 9);
        Assert.True(result.Length == 2);
    }
        
    [Fact]
    public void Test2()
    {
        var result = TwoSumSolution.TwoSum(new int[]{3,3}, 6);
        Assert.True(result.Length == 2);
    }

    [Fact]
    public void TestThreeSum1()
    {
        var sol = new ThreeSumSolution();
        var result = sol.ThreeSum([-1, 0, 1, 2, -1, 4]);
        Assert.True(result.Count == 1);
    }

    [Fact]
    public void TestCanFinishCourse()
    {
        var sol = new CanFinishCoursesSolution();
        int[][] jaggedArray = 
        [
            [1, 0]
        ];
        var result = sol.CanFinish(2, jaggedArray);
        Assert.True(result);
    }

    [Fact]
    public void TestRegexParse()
    {
        var sol = new RegexParseSolution();
        
        var result = sol.IsMatch("aa", "a*");
        Assert.True(result);

        result = sol.IsMatch("ab", ".*c");
        Assert.False(result);
    }
    [Fact]
    public void TestMaze()
    {
        var sol = new MazeSolution();
        var maze = new int[6,6];
        IList<Cordinate> path;
        var result = sol.HasPath(maze, out path);
        Assert.True(path.Any());
    }

    [Fact]
    public void TestTopK()
    {
        var dict = new Dictionary<char, int>();
        dict['a'] = 1;
        dict['b']++;

        var solution = new TopKFrequentSolution();
        var res = solution.TopKFrequent([1,2,3,3,4,4,4,5], 2);
        Assert.True(res.Count == 2);
    }

    [Fact]
    public void TestDictionary()
    {
        var dict = new Dictionary<char, int>();
        dict['a'] = 1;
        dict['b']++;
    }
}