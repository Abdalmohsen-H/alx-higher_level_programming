#!/usr/bin/python3
# task 1 code


def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    for indx in range(len(my_list)):
        if idx == indx:
            return my_list[indx]
