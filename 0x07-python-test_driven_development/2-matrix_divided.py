#!/usr/bin/python3
'# a function that divides all elements of a matrix'


def matrix_divided(matrix, div):
    '# verification of an empty matrix'
    if not matrix:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for sub in matrix:
        if not isinstance(sub, list):
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if not sub:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        for num in sub:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    size = len(matrix[0])
    for lists in matrix:
        if len(lists) != size:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    nw = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return nw
