class ReverseOnlyLetters:
    def reverse_only_letters(self, value: str) -> str:
        letters, result = [character for character in value if character.isalpha()], []
        for character in value: result.append(letters.pop() if character.isalpha() else character)
        return "".join(result)
