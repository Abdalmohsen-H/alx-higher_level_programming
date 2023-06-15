#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # task 15 (102-com*del*.py) : del items of dict has certain val
    nw_dict = a_dictionary
    for ky, val in nw_dict.copy().items():
        if val == value:
            del nw_dict[ky]
        # print(len(a_dictionary))
        # print(nw_dict)
    return nw_dict


"""
def print_sorted_dictionary(a_dictionary):
    # task 6 : sort dict and print ky , vals
    for ky in sorted(a_dictionary):
        print("{}: {}".format(ky, a_dictionary[ky]))


a_dictionary={'lang':"C",'track':"Low",'pref':"C",'ids':[1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
"""
