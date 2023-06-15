#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # task 11 : mul. items of list without loops
    return list(map(lambda x: x * number, my_list))


"""
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
"""
