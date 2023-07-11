#!/usr/bin/python3
''' a module that have a class student '''


import json


class Student():
    ''' class student for task 11 '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' returns obj.__dict__'''
        try:
            nwlst = {}
            for itm in attrs:
                if itm in self.__dict__:
                    nwlst[itm] = self.__dict__[itm]
                if type(itm) != str:
                    return self.__dict__
            return nwlst

        except Exception:
            return self.__dict__

    def reload_from_json(self, inptjson):
        ''' override values of the instance attributes
        with values from json
        '''
        if type(inptjson) != dict:
            nwdict = json.loads(inptjson)
        else:
            nwdict = inptjson

        for ky, val in nwdict.items():
            # print(f"key {ky} : val {val}")
            if ky in self.__dict__:
                self.__dict__[ky] = val
