#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # better time complexity for List comprehension: O(n),
    # where n is the number of elements in the matrix.
    return [[(elmnt**2) for elmnt in row] for row in matrix]
    """
    #another methods
    #1st method another list comprehension usin map, lambda, list
    # return [list(map(lambda elm: elm*elm, mrow)) for mrow in matrix]
    # 2nd method --- > Nested loops: O(n^2)
    nwlst = matrix  # to avoid error out of range for non
    # intialized list like nwlst = [] when try to assign using index
    # for rownum, rowdata in enumerate(matrix):
    # the below line also equivalent to the above commented line
    for rowdata , rownum in zip(matrix, range(len(matrix))):
        nwlst[rownum] = [elmnt**2 for elmnt in rowdata]
    return nwlst
    """


"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(square_matrix_simple(matrix))
"""
