// https://leetcode.com/problems/time-based-key-value-store/description/
public class TimeMap {
    private readonly Dictionary<string, List<(string value, int timestamp)>> keyStore;

    /** Initialize your data structure here. */
    public TimeMap() {
        keyStore = [];
    }

    public void Set(string key, string value, int timestamp) {
        if (!keyStore.ContainsKey(key)) {
            keyStore[key] = [];
        }
        keyStore[key].Add((value, timestamp));
    }

    public string Get(string key, int timestamp) {
        if (!keyStore.ContainsKey(key)) {
            return "";
        }

        List<(string value, int timestamp)> values = keyStore[key];
        string res = "";
        int l = 0, r = values.Count - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            if (values[m].timestamp == timestamp) {
                return values[m].value;
            }
            else if (values[m].timestamp < timestamp) {
                res = values[m].value;
                l = m + 1;
            } 
            else {
                r = m - 1;
            }
        }

        return res;
    }
}
