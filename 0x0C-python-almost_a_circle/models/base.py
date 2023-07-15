#!/usr/bin/python3
'''
task 1 module doc, create class base
a. Hesham
'''


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
