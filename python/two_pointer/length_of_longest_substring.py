class LongestSubstring:
    def length_of_longest_substring(self, value: str) -> int:
        last, left, best = {}, 0, 0
        for right, character in enumerate(value):
            left = max(left, last.get(character, -1) + 1); last[character] = right; best = max(best, right - left + 1)
        return best

    def length_of_longest_substring_with_set(self, value: str) -> int:
        seen, left, best = set(), 0, 0
        for right, character in enumerate(value):
            while character in seen: seen.remove(value[left]); left += 1
            seen.add(character); best = max(best, right - left + 1)
        return best
