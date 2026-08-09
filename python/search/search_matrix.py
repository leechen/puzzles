class MatrixSearch:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        columns, left, right = len(matrix[0]), 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2; value = matrix[middle // columns][middle % columns]
            if value == target: return True
            if value < target: left = middle + 1
            else: right = middle - 1
        return False

    def search_matrix_two_phase(self, matrix: list[list[int]], target: int) -> bool:
        return self.search_matrix(matrix, target)
