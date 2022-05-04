#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    count = 0
    b = 0
    for i in matrix:
        new.append([])
        for j in i:
            b = j * j
            new[count].append(b)
            b = 0
        count = count + 1
    return new
