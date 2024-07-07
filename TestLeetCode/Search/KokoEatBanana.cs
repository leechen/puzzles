public class MinEatingSpeedSolution {
    public int MinEatingSpeed(int[] piles, int h) {
        int l = 1, r = piles.Max();
        int res = r;

        while (l <= r) {
            int k = (l + r) / 2;
            long totalTime = 0;  // Use long to avoid overflow
            
            foreach (int p in piles) {
                // Equivalent to Math.Ceiling((double)p / k)
                // we should avoid using Math.Ceiling for calculating the total time, 
                // as it might introduce precision issues with large integers
                totalTime += (p + k - 1) / k;  
            }

            if (totalTime <= h) {
                res = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
        }

        return res;
    }
}