import heapq
from python.common import Interval


class MinimumMeetingRooms:
    def min_meeting_rooms(self, intervals: list[Interval]) -> int:
        ends = []
        for interval in sorted(intervals, key=lambda item: item.start):
            if ends and ends[0] <= interval.start: heapq.heapreplace(ends, interval.end)
            else: heapq.heappush(ends, interval.end)
        return len(ends)
