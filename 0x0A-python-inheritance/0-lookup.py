#!/usr/bin/python3
''' a module that have a function
that takes an object as input
Task 0 : A. Hesham
returns all existed methods and attributes
inside the object
'''


def lookup(obj):
    ''' a function that return methods and attributes
    return of type list
    '''
    return dir(obj)
