from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0: raise ValueError("capacity must be positive")
        self.capacity, self.data = capacity, OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        self.data.move_to_end(key); return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data: self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity: self.data.popitem(last=False)
