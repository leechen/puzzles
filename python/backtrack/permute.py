class Permutations:
    def permute(self, numbers: list[int]) -> list[list[int]]:
        result = [[]]
        for value in numbers:
            result = [path[:index] + [value] + path[index:] for path in result for index in range(len(path) + 1)]
        return result

    def permute_recursive(self, numbers: list[int]) -> list[list[int]]:
        result = []
        def visit(start: int) -> None:
            if start == len(numbers):
                result.append(numbers.copy()); return
            for index in range(start, len(numbers)):
                numbers[start], numbers[index] = numbers[index], numbers[start]
                visit(start + 1)
                numbers[start], numbers[index] = numbers[index], numbers[start]
        visit(0)
        return result
