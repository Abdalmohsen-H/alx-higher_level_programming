#!/usr/bin/python3
''' a module that have a function
that takes an object & class as input
Task 2 : A. Hesham
returns True if the oject is
an instance of the class
else false
'''


def is_same_class(obj, a_class):
    ''' a function that checks if object is
    an instance of the class
    return True or False
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
