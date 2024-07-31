public class DailyTemperaturesSolution
{
    public int[] DailyTemperatures(int[] temperatures)
    {
        int[] res = new int[temperatures.Length];

        // This is a good example of new C# feature without using a POCO class.
        // (int temp, int index) is equivalent to the new class type
        Stack<(int temp, int index)> stack = new Stack<(int, int)>();

        for (int i = 0; i < temperatures.Length; i++)
        {
            int t = temperatures[i];
            while (stack.Count > 0 && t > stack.Peek().temp)
            {
                var (_, index) = stack.Pop();
                res[index] = i - index;
            }
            // notice that here, we need double ()
            stack.Push((t, i));
        }
        return res;
    }
}
