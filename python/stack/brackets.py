class ValidBrackets:
    def is_valid(self, value: str) -> bool:
        matching, stack = {")": "(", "]": "[", "}": "{"}, []
        for character in value:
            if character in matching:
                if not stack or stack.pop() != matching[character]: return False
            else: stack.append(character)
        return not stack
