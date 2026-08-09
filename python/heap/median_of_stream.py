import heapq


class MedianFinder:
    def __init__(self): self.lower, self.upper = [], []

    def add_num(self, number: int) -> None:
        heapq.heappush(self.lower, -number)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.upper) > len(self.lower): heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def find_median(self) -> float:
        if not self.lower: raise ValueError("no numbers available")
        if len(self.lower) > len(self.upper): return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2
