#!/usr/bin/python3
"""matrix_divided

"""


def matrix_divided(matrix, div):
    """matrix_divided
    arg:
        matrix: matrix of integer number
        div: number
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all((len(row) == len(matrix[0])) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round((elemnt / div), 2) for elemnt in row] for row in matrix]
    return new
