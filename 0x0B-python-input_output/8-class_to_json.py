#!/usr/bin/python3
''' a module that have a function
takes an object (an instance of a Class)
as input, then returns the dictionary description
with simple data structure (list, dictionary, integer,
string and boolean)
for JSON serialization of an object
A. Hesham
task 8
'''


def class_to_json(obj):
    ''' function takes an object as input, then returns
    the dictionary description with simple data
    structure (list, dictionary, integer, string and boolean)
    for JSON serialization of an object
    A. Hesham
    task 8
    obj is instance of a class
    '''
    return obj.__dict__
