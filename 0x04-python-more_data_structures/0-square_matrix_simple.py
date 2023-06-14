#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # return [[row[i] for row in matrix] for i in range(3)]
    if not matrix or not matrix[0]:
        return
    return [[row[i]**2 for i in range(len(matrix))] for row in matrix]
