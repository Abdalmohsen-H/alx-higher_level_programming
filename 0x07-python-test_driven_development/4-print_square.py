#!/usr/bin/python
'''print square using #'s in stdout'''


def print_square(size):
    '''
    print square using #'s in stdout
    '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    # print square using #'s in stdout
    print_symbol = '#'
    if size == 0:
        print("")
    else:
        for Vunit in range(size):
            for Hunit in range(size):
                print("{}".format(print_symbol), end="")
            if Vunit < size:
                print("\n", end="")
    return ""
