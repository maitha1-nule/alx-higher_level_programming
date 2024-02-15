#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for a, row in enumerate(new_matrix):
        for b, col in enumerate(new_matrix):
            new_matrix[a][b] = row[b] ** 2
    return new_matrix
