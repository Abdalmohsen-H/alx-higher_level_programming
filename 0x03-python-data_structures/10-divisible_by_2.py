#!/usr/bin/python3
# task 10 code


def divisible_by_2(my_list=[]):
    if (my_list is None) or len(my_list) < 1:
        return None
    divlist = []
    for indx, elem in enumerate(my_list):
        if (elem % 2) == 0:
            divlist.append(1)
        else:
            divlist.append(0)
    return (divlist)
