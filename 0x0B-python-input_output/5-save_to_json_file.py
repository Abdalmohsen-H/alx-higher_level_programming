#!/usr/bin/python3
''' a module that have a function
takes an object and filename as inputs
then write it to a text file.
A. Hesham
'''


import json


def save_to_json_file(my_obj, filename):
    ''' function takes an object and filename
    to write it to a text file.
    any Python object that can be serialized as JSON,
    such as dictionaries, lists, or custom objects.
    '''
    if len(filename) > 0:
        mode = "w"  # must be write mode to write to the file
        with open(filename, mode, encoding="utf-8") as file:
            json.dump(my_obj, file)
