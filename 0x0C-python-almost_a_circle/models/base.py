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

    @staticmethod
    def from_json_string(json_string):
        ''' take json string representing a list of dictionaries
        return actual list of dictionaries
        '''
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' class method takes a dict with attrs
        then creat "dummy" instance with attrs and values from dict
        Return: this "dummy" instance
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # dummy values
        if cls.__name__ == "Square":
            dummy = cls(1)  # dummy values
        dummy.update(**dictionary)  # update the dummy "instance"->important
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' classs method : read json file for this class
        created before if exist , it will read list of instance and attrs
        then create instances using above create , from_json_string methods
        return: list of instances
        '''
        filename = f"{cls.__name__}.json"
        inst_list = []
        try:
            with open(filename, "r") as file:
                jsn_str = file.read()
                dictList = cls.from_json_string(jsn_str)
                for dict in dictList:
                    inst_list.append(cls.create(**dict))
                return inst_list
        except Exception as e:  # FileNotFoundError
            return []
