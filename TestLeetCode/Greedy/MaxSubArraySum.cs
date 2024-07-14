public class MaxSubArraySolution {
    public int MaxSubArray(int[] array) {
            if (array == null || array.Length == 0) return Int32.MinValue;
            int curMax = array[0];

            int curSum = 0;
            foreach (int x in array)
            {
                curSum += x;
                if (curSum > curMax) curMax = curSum;
                if (curSum < 0) curSum = 0;
            }

            return curMax;        
    }
}