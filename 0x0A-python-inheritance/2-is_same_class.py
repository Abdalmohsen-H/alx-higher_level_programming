#!/usr/bin/python3
''' a module that have a function
that takes an object & class as input
Task 2 : A. Hesham
returns True if the oject is
an (exact) instance of the class
else false
the imporatnt keyword here is "exact instance"
'''


def is_same_class(obj, a_class):
    ''' a function that checks if object is
    an (exact) instance of the class
    return True or False
    '''
    return type(obj) == a_class
