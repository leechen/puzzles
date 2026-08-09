class GenerateParentheses:
    def generate_parenthesis(self, n: int) -> list[str]:
        result = []
        def visit(opened: int, closed: int, path: str) -> None:
            if len(path) == 2 * n: result.append(path); return
            if opened < n: visit(opened + 1, closed, path + "(")
            if closed < opened: visit(opened, closed + 1, path + ")")
        visit(0, 0, "")
        return result
