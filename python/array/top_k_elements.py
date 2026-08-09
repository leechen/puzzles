from collections import Counter


class TopKFrequent:
    def top_k_frequent(self, numbers: list[int], k: int) -> list[int]:
        return [value for value, _ in Counter(numbers).most_common(k)]
