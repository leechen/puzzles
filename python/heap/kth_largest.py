import heapq


class KthLargest:
    def __init__(self, k: int, numbers: list[int]):
        if k <= 0: raise ValueError("k must be positive")
        self.k, self.heap = k, numbers.copy()
        heapq.heapify(self.heap)
        while len(self.heap) > k: heapq.heappop(self.heap)

    def add(self, value: int) -> int:
        heapq.heappush(self.heap, value)
        if len(self.heap) > self.k: heapq.heappop(self.heap)
        return self.heap[0]
