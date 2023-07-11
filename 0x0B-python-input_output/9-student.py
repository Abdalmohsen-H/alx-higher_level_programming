#!/usr/bin/python3
''' a module that have a class student '''


class Student():
    ''' class student for task 9 '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
