class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            # this is a nice syntax to avoid the if else statement, 
            # it will return the value of the key if it exists, otherwise it will return 0
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts:
                return False

            counts[char] -= 1

            if counts[char] == 0:
                del counts[char]

        return not counts
        