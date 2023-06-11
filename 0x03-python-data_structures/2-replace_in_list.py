#!/usr/bin/python3
# task 1 code


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    for indx in range(len(my_list)):
        if idx == indx and element:  # check if elem is valid
            my_list[indx] = element
            return my_list
