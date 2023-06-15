#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda mrow: list(map(lambda i: i * i, mrow)), matrix))
