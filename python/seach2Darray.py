from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1

        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // columns][middle % columns]
            if value == target:
                return True
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        return False


def main() -> None:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(Solution().searchMatrix(matrix, 3))


if __name__ == "__main__":
    main()
