#!/usr/bin/python3
''' a module that have a function
takes input represented by a JSON string
returns an object (object data structure in Python)
'''


import json


def to_json_string(my_obj):
    ''' function takes JSON string representation of an object
    returns an object (object data structure in Python)
    '''
    return json.loads(my_obj)
