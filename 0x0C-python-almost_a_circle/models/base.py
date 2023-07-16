#!/usr/bin/python3
'''
task 1 module doc, create class base
a. Hesham
'''


import json


class Base():
    ''' Base class for task 1'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor to intialize objects(instances)'''
        if id is not None:
            self.id = id

        else:
            # print(f"id is none, __nb_objects before == {Base.__nb_objects}")
            Base.__nb_objects += 1  # must refer to base class(not obj's self)
            # base increnment in the class with every new obj where id is none
            self.id = Base.__nb_objects
            # print(f"id is {id},__nb_objects after == {Base.__nb_objects}")

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' take list of dicts and returns json '''
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save json of list_obj to a file
        named after the obj's class name
        but you must get dict of each object first
        '''
        file_name = f"{cls.__name__}.json"
        with open(file_name, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                json.dump([], file)
            else:
                list_ofdicts = []
                dicto = {}
                for obj in list_objs:
                    dicto = cls.to_dictionary(obj)
                    list_ofdicts.append(dicto)
                text = cls.to_json_string(list_ofdicts)
                file.write(text)
