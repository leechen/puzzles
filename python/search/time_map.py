from bisect import bisect_right


class TimeMap:
    def __init__(self): self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.values.get(key, [])
        index = bisect_right(entries, (timestamp, chr(0x10FFFF))) - 1
        return entries[index][1] if index >= 0 else ""
