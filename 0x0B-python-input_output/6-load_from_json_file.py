#!/usr/bin/python3
''' a module that have a function
takes a json file's name as input
then return created bject based on this
JSON string from the JSON file
A. Hesham
'''


import json


def load_from_json_file(filename):
    ''' function takes takes a json file's name as input
    then return created bject based on this
    JSON string from the JSON file
    any Python object that can be serialized as JSON,
    such as dictionaries, lists, or custom objects.
    '''
    if len(filename) > 0:
        mode = "r"
        with open(filename, mode, encoding="utf-8") as file:
            return json.load(file)
