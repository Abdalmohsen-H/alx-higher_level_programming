#!/usr/bin/python3
def uniq_add(my_list=[]):
    # task no. 2
    #  return sum of unique elements of a list.
    sum = 0
    if len(my_list) < 1:
        return None
    for elem in set(my_list):  # use set to get unique elements
        sum = sum + elem
    return sum


"""
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
"""
