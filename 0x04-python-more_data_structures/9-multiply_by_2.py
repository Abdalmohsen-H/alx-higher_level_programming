#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # task 9 : return dict after multipla all vals by 2
    nw_dict = {}
    for ky, val in a_dictionary.items():
        nw_dict[ky] = val * 2
    return nw_dict
