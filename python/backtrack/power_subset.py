class Subsets:
    def subsets(self, numbers: list[int]) -> list[list[int]]:
        result = [[]]
        for value in numbers:
            result += [subset + [value] for subset in result]
        return result
