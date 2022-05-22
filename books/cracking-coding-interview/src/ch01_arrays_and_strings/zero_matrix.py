from typing import List

import pytest


def nullify_loop(matrix: List[List[int]]) -> List[List[int]]:
    height, width = len(matrix), len(matrix[0])
    columns, rows = set(), set()

    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 0:
                columns.add(col)
                rows.add(row)

    return [
        [
            0 if row in rows or col in columns else matrix[row][col]
            for col in range(width)
        ]
        for row in range(height)
    ]


def nullify_in_place(matrix: List[List[int]]) -> List[List[int]]:
    height, width = len(matrix), len(matrix[0])

    def nullify_column(pos: int) -> None:
        for i in range(height):
            matrix[i][pos] = 0

    def nullify_row(pos: int) -> None:
        matrix[pos] = [0] * width

    col_start = 0

    for row in range(height):
        for col in range(col_start, width):
            if matrix[row][col] == 0:
                nullify_row(row)
                nullify_column(col)

                col_start = col + 1
                break

    return matrix


@pytest.mark.parametrize("matrix, rotated_matrix", [
    ([[0, 2],
      [3, 4]],
     [[0, 0],
      [0, 4]]),
    ([[1, 2, 3, 4],
      [1, 0, 3, 4],
      [1, 2, 3, 0]],
     [[1, 0, 3, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]])
])
@pytest.mark.parametrize("function", [
    nullify_loop,
    nullify_in_place,
])
def test_algorithm(function, matrix, rotated_matrix):
    assert function(matrix) == rotated_matrix
