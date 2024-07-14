
 // * Definition of Interval:
 public class Interval {
    public int start, end;
    Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class CanAttendMeetingsSolution {
        public bool CanAttendMeetings(List<Interval> intervals) {   
            if (intervals == null || intervals.Count <= 1 ) { return true; }
            intervals.Sort((a, b) => a.start - b.start);
            for (int i = 1; i < intervals.Count; i++)
            {
                if (intervals[i].start < intervals[i - 1].end)
                {
                    return false;
                }
            }
            return true;
        }
}