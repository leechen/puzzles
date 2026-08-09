import pytest

from python.seach2Darray import Solution, main


MATRIX = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


@pytest.mark.parametrize("target", [1, 3, 11, 60])
def test_search_matrix_finds_values(target):
    assert Solution().searchMatrix(MATRIX, target)


@pytest.mark.parametrize("target", [-1, 2, 13, 61])
def test_search_matrix_rejects_missing_values(target):
    assert not Solution().searchMatrix(MATRIX, target)


@pytest.mark.parametrize("matrix", [[], [[]]])
def test_search_matrix_handles_empty_matrix(matrix):
    assert not Solution().searchMatrix(matrix, 1)


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "True\n"
