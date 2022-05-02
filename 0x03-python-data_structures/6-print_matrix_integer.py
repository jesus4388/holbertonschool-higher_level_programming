#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if j < len(matrix) - 1:
                print(f"{matrix[i][j]}", end=" ")
            else:
                print(f"{matrix[i][j]}", end="\n")
