from python.common import Interval


class MeetingRooms:
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        ordered = sorted(intervals, key=lambda item: item.start)
        return all(current.start >= previous.end for previous, current in zip(ordered, ordered[1:]))
