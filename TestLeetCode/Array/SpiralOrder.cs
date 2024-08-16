
class SpiralOrderSolution
{
    int[] GetSpiralOrder(int[][] input)
    {
        if (input == null) { return new int[0]; }
        int len = input.Length;  // m = 3
        int wid = input[0].Length; // n = 4
        int size = len * wid;
        int[] result = new int[size];

        int i = 0;
        int j = 0;
        int layer = 0;
        int count = 0;

        while (count < size)
        {
            for (int k = layer; k < wid - layer; k++)
            { // k 0,1,2
                // going right
                i = layer; // index = 0-3 => 0
                j = k; //index = 0,1,2,3. => 0 -> 3
                result[count] = input[i][j];
                count++;
            }
            // going down
            for (int k = layer; k < len - layer; k++)
            { // 0 - 3
                i = wid - 1 - layer;
                j = k;
                result[count] = input[i][j];
                count++;
            }
            /*
// Input: matrix = [[1,2,3],
//                  [4,5,6],
//                  [7,8,9],
//                  [10,11,12]]
            */
            for (int k = wid - 2 - layer; k >= layer; k--)
            {
                // going left
                i = len - layer; // index = 0-3 => 3
                j = k; // 1,0
                result[count] = input[i][j];
                count++;
            }
            // going up
            for (int k = len - 2 - layer; k > layer; k--)
            {
                i = k;
                j = layer;
                result[count] = input[i][j];
                count++;
            }
            layer++;
        }

        return result;
    }
}