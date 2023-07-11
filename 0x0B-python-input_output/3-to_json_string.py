#!/usr/bin/python3
''' a module that have a function takes an object
returns JSON string representation of an object
'''


import json


def to_json_string(my_obj):
    ''' function take an object
    i.e. (returns JSON string representation of an object)
    '''
    return json.dumps(my_obj)
