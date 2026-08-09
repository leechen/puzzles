from collections import defaultdict


class CharacterReplacement:
    def character_replacement(self, value: str, k: int) -> int:
        counts, left, most, best = defaultdict(int), 0, 0, 0
        for right, character in enumerate(value):
            counts[character] += 1; most = max(most, counts[character])
            while right - left + 1 - most > k: counts[value[left]] -= 1; left += 1
            best = max(best, right - left + 1)
        return best
