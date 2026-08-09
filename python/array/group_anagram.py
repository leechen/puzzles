from collections import defaultdict


class GroupAnagrams:
    def group_anagrams(self, strings: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for value in strings:
            counts = [0] * 26
            for character in value:
                counts[ord(character) - ord("a")] += 1
            groups[tuple(counts)].append(value)
        return list(groups.values())
