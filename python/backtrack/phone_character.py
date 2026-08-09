class LetterCombinations:
    DIGITS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        result = [""]
        for digit in digits:
            result = [prefix + character for prefix in result for character in self.DIGITS[digit]]
        return result
