#!/usr/bin/python3
# task 4 code


def new_in_list(my_list, idx, element):
    nw_list = my_list.copy()  # or my_list[:]
    if idx < 0 or idx > (len(nw_list) - 1):
        return nw_list
    for indx in range(len(nw_list)):
        if idx == indx and element:  # check if elem is valid
            nw_list[indx] = element
            return nw_list
