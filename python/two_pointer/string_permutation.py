from collections import Counter


class PermutationInString:
    def check_inclusion(self, pattern: str, value: str) -> bool:
        if len(pattern) > len(value): return False
        target, window = Counter(pattern), Counter(value[: len(pattern)])
        if target == window: return True
        for index in range(len(pattern), len(value)):
            window[value[index]] += 1; outgoing = value[index - len(pattern)]; window[outgoing] -= 1
            if not window[outgoing]: del window[outgoing]
            if window == target: return True
        return False
