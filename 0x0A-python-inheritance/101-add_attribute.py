#!/usr/bin/python3
''' a module that have a func
checks wether obj's class excepts
adding new attributes or not
Task 101 : A. Hesham
'''


def add_attribute(obj, attr, value):
    ''' add attribute to a class
    Task 101 : A. Hesham
    '''
    if hasattr(obj, '__dict__'):  # accept adding attributes
        setattr(obj, attr, value)
    else:  # class doesn't allow adding attributes
        raise TypeError("can't add new attribute")
