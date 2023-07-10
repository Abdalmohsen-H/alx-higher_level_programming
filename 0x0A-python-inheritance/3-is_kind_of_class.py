#!/usr/bin/python3
''' a module that have a function
that takes an (object or a class) &
another class as input
Task 2 : A. Hesham
returns True if 1st input is subclass of input 2
returns True if 1st input is intance of input 2
else false
'''


def is_kind_of_class(obj, a_class):
    ''' a function that checks if object or class
    is instance or subclass other class
    return True or False
    '''
    try:
        return issubclass(obj, a_class)
    except Exception as e:
        return isinstance(obj, a_class)
