#!/usr/bin/python3
# task 9 code


def max_integer(my_list=[]):
    if (my_list is None) or len(my_list) < 1:  # empty list, i.e. len = 0
        return None
    my_list.sort()
    maxvalindx = len(my_list) - 1
    maxval = my_list[maxvalindx]
    return (maxval)


"""
my_list1 = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list1)
print("Max: {}".format(max_value))
"""
