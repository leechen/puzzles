public class TopKFrequentSolution {
        public IList<int> TopKFrequent(int[] nums, int k)
        {
            int len = nums.Length;
            List<int>[] bucket = new List<int>[len+1];
            Dictionary<int, int> frequencyMap = new Dictionary<int, int>();

            foreach (int n in nums)
            {
                if (!frequencyMap.ContainsKey(n)) { frequencyMap.Add(n, 0); }
                frequencyMap[n]++;
            }

            foreach (var item in frequencyMap)
            {
                int frequency = item.Value;
                if (bucket[frequency] == null)
                {
                    bucket[frequency] = new List<int>();
                }
                bucket[frequency].Add(item.Key);
            }

            List<int> res = new List<int>();

            for (int pos = bucket.Length - 1; pos >= 0 && res.Count < k; pos--)
            {
                if (bucket[pos] != null)
                {
                    res.AddRange(bucket[pos]);
                }
            }
            return res;
        }
}
