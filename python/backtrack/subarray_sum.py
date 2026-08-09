class CombinationSum:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def visit(index: int, total: int, path: list[int]) -> None:
            if total == target:
                result.append(path.copy()); return
            if total > target or index == len(candidates):
                return
            path.append(candidates[index]); visit(index, total + candidates[index], path); path.pop()
            visit(index + 1, total, path)
        visit(0, 0, [])
        return result
