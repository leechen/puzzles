from functools import cache


class RegexMatcher:
    def is_match(self, text: str, pattern: str) -> bool:
        @cache
        def match(text_index: int, pattern_index: int) -> bool:
            if pattern_index == len(pattern):
                return text_index == len(text)
            first = text_index < len(text) and pattern[pattern_index] in {text[text_index], "."}
            if pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
                return match(text_index, pattern_index + 2) or first and match(text_index + 1, pattern_index)
            return first and match(text_index + 1, pattern_index + 1)
        return match(0, 0)
