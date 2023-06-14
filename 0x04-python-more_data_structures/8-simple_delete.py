#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # task 8 : del one item of dict
    try:
        del a_dictionary[key]
    except Exception as e:  # to avoid "don't use bare except" py style error
        pass
    return a_dictionary


"""
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
"""
