class ProductExceptSelf:
    def product_except_self(self, numbers: list[int]) -> list[int]:
        result = [1] * len(numbers)
        prefix = 1
        for index, value in enumerate(numbers):
            result[index] = prefix
            prefix *= value
        suffix = 1
        for index in range(len(numbers) - 1, -1, -1):
            result[index] *= suffix
            suffix *= numbers[index]
        return result
