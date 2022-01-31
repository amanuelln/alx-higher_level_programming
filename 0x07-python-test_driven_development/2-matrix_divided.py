#!/usr/bin/python3
"""
This is the matrix_divided module.

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.

    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): the divider, >= 0.
    """
    mtrx_type_err = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_len_err = 'Each row of the matrix must have the same size'
    div_type_err = 'div must be a number'
    div_zero_err = 'division by zero'

    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_err)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_err)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_err)
        if len(row) is not row_len and row_len is not 0:
            raise TypeError(mtrx_len_err)
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError(div_type_err)
    if div is 0:
        raise ZeroDivisionError(div_zero_err)

    return [[round(nb / div, 2) for nb in row] for row in matrix]
