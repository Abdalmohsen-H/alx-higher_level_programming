#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # task 6 : sort dict and print ky , vals
    for ky in sorted(a_dictionary):
        print("{}: {}".format(ky, a_dictionary[ky]))
