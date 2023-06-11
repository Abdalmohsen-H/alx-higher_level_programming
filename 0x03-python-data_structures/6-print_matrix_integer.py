#!/usr/bin/python3
# task 6 code


def print_matrix_integer(matrix=[[]]):
    for row, sublist in enumerate(matrix):
        for idx, subelem in enumerate(sublist):
            print("{:d}".format(subelem), end="")
            if idx+1 < len(sublist):
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
