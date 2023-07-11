#!/usr/bin/python3
''' a module that have a function
returns JSON representation of an object
    i.e. (returns string)
'''


import json


def to_json_string(my_obj):
    ''' functions returns JSON representation of an object
    i.e. (returns string)
    '''
    return json.dumps(my_obj)
