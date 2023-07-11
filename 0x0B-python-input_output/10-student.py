#!/usr/bin/python3
''' a module that have a class student '''


class Student():
    ''' class student for task 9 '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
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
