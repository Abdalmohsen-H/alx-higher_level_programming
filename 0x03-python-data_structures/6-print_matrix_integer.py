#!/usr/bin/python3
# task 6 code


def print_matrix_integer(matrix=[[]]):
    for idx, elem in enumerate(matrix):
        for idx, subelem in enumerate(elem):
            print(f"{subelem}", end="")
            if idx+1 < len(elem):
                print(" ", end="")
        print("")


"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
"""
