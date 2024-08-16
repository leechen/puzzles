class SpiralOrderSolution
{
    public int[] GetSpiralOrder(int[][] input)
    {
        if (input == null || input.Length == 0) return new int[0];

        int len = input.Length;  // m = 4
        int wid = input[0].Length; // n = 3
        int size = len * wi;
        int[] result = new int[size];

        int layer = 0;
        int count = 0;

        while (count < size)
        {
            // Going right
            for (int j = layer; j < wid - layer && count < size; j++)
            {
                result[count] = input[layer][j];
                count++;
            }

            // Going down
            for (int i = layer + 1; i < len - layer && count < size; i++)
            {
                result[count] = input[i][wid - layer - 1];
                count++;
            }

            // Going left
            for (int j = wid - layer - 2; j >= layer && count < size; j--)
            {
                result[count] = input[len - layer - 1][j];
                count++;
            }

            // Going up
            for (int i = len - layer - 2; i > layer && count < size; i--)
            {
                result[count] = input[i][layer];
                count++;
            }

            layer++;
        }

        return result;
    }
}
