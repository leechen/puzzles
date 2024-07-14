/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */
namespace lintcode
{
    class MinMeetingRoomsSolution {
        /**
         * @param intervals: an array of meeting time intervals
         * @return: the minimum number of conference rooms required
         */
        public int MinMeetingRooms(List<Interval> intervals) {
            var starts = intervals.Select(i => i.start).ToList();
            var ends = intervals.Select(i => i.end).ToList();

            starts.Sort();
            ends.Sort();
            
            int startPointer = 0, endPointer = 0;
            int usedRooms = 0;
            int result = 0;

            while (startPointer < starts.Count) {
                if (starts[startPointer] < ends[endPointer]) {
                    usedRooms++;
                    startPointer++;
                } else {
                    usedRooms--;
                    endPointer++;
                }
                result = Math.Max(result, usedRooms);
            }

            return result;
        }
    }
}