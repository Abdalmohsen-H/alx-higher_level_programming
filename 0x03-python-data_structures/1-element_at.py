#!/usr/bin/python3
foundindx = 0


def element_at(my_list, idx):
    for indx in range(len(my_list)):
        if idx == indx:
            foundindx = 1
            return my_list[indx]
    if foundindx != 1:
        return None
