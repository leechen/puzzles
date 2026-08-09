class ValidPalindrome:
    def is_palindrome(self, value: str) -> bool:
        filtered = [character.casefold() for character in value if character.isalnum()]
        return filtered == filtered[::-1]

    def is_palindrome_two_pointer(self, value: str) -> bool:
        left, right = 0, len(value) - 1
        while left < right:
            if not value[left].isalnum(): left += 1
            elif not value[right].isalnum(): right -= 1
            elif value[left].casefold() != value[right].casefold(): return False
            else: left += 1; right -= 1
        return True
