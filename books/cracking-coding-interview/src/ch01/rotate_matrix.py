from typing import List

import pytest


def rotate_matrix_list_comprehension(matrix: List[List[int]]) -> List[List[int]]:
    size = len(matrix)
    return [
        [matrix[col][row] for col in reversed(range(size))]
        for row in range(size)
    ]


def rotate_matrix_zip(matrix: List[List[int]]) -> List[List[int]]:
    return [list(reversed(row)) for row in zip(*matrix)]


@pytest.mark.parametrize("matrix, rotated_matrix", [
    ([[1, 2],
      [3, 4]],
     [[3, 1],
      [4, 2]]),
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]]),
    ([[1, 2, 3, 8],
      [4, 5, 6, 8],
      [7, 8, 9, 8],
      [8, 8, 8, 8]],
     [[8, 7, 4, 1],
      [8, 8, 5, 2],
      [8, 9, 6, 3],
      [8, 8, 8, 8]])
])
@pytest.mark.parametrize("function", [
    rotate_matrix_zip,
    rotate_matrix_list_comprehension
])
def test_algorithm(function, matrix, rotated_matrix):
    assert function(matrix) == rotated_matrix
