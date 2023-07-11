#!/usr/bin/python3
''' a module that have imports function
takes bash args as input
save it to file
then return created bject based on this
JSON string from the JSON file
A. Hesham
'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def get_args(obj):
    ''' function takes takes bash args as input
    save it to file
    then return created bject based on this
    JSON string from the JSON file
    any Python object that can be serialized as JSON,
    such as dictionaries, lists, or custom objects.
    '''
    filename = "add_item.json"  # must be of type string
    try:
        lst = load_from_json_file(filename)
        lst.extend(obj)  # add new args list to old args list
    except Exception as e:
        print(f"{e.__class__.__name__} : {e}")
        lst = obj
    save_to_json_file(lst, filename)


if __name__ == '__main__':
    obj = list(sys.argv[1:])
    get_args(obj)
    # print(f"get argv : {obj}")
