class NonOverlappingIntervals:
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        removed, end = 0, float("-inf")
        for start, current_end in sorted(intervals, key=lambda item: item[1]):
            if start < end: removed += 1
            else: end = current_end
        return removed
