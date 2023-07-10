#!/usr/bin/python3
''' a module that have an empty class
Task 6 : A. Hesham
'''


class BaseGeometry():
    ''' class raises Exception with msg
    on pub func
    '''

    def area(self):
        raise Exception('area() is not implemented')
