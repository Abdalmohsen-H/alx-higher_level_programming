#!/usr/bin/python3
''' a module that have a function
takes input represented by a JSON string
returns an object (object data structure in Python)
'''


import json


def from_json_string(my_str):
    ''' function takes JSON string representation of an object
    returns an object (object data structure in Python)
    '''
    return json.loads(my_obj)
