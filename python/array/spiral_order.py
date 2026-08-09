class SpiralOrder:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            result.extend(matrix[top][left : right + 1])
            top += 1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                result.extend(reversed(matrix[bottom][left : right + 1]))
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result

    def spiral_order_iterative(self, matrix: list[list[int]]) -> list[int]:
        return self.spiral_order(matrix)
