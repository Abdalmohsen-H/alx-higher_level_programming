#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # task 1
    #  replace all occurrences of an elem.
    # by another in a new list, then return new list
    nwlst = my_list.copy()
    for indx, elem in enumerate(my_list):
        if elem == search:
            nwlst[indx] = replace
    return nwlst


"""
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
"""
