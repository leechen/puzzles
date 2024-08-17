// 

class SpiralOrderSolution
{
    public int[] GetSpiralOrder(int[][] input)
    {
        if (input == null || input.Length == 0) return new int[0];

        int len = input.Length;  // m = 4
        int wid = input[0].Length; // n = 3
        int size = len * wid;
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
    
   public IList<int> SpiralOrder2(int[][] matrix)
    {
        // Handle edge case of empty or null matrix
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0) 
        { 
            return new List<int>(); 
        }

        List<int> res = new List<int>();
        int currentRow = 0, currentCol = 0;
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        while (currentRow < rows && currentCol < cols)
        {
            // Traverse from left to right across the top row
            for (int i = currentCol; i < cols; ++i)
            {
                res.Add(matrix[currentRow][i]);
            }
            currentRow++;

            // Traverse from top to bottom along the right column
            for (int i = currentRow; i < rows; ++i)
            {
                res.Add(matrix[i][cols - 1]);
            }
            cols--;

            // Traverse from right to left across the bottom row, if applicable
            if (currentRow < rows)
            {
                for (int i = cols - 1; i >= currentCol; --i)
                {
                    res.Add(matrix[rows - 1][i]);
                }
                rows--;
            }

            // Traverse from bottom to top along the left column, if applicable
            if (currentCol < cols)
            {
                for (int i = rows - 1; i >= currentRow; --i)
                {
                    res.Add(matrix[i][currentCol]);
                }
                currentCol++;
            }
        }

        return res;
    }

}