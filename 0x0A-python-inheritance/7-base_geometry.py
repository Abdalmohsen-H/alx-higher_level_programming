#!/usr/bin/python3
''' a module that have an empty class
Task 7 : A. Hesham
'''


class BaseGeometry():
    ''' class raises Exception with msg
    on pub func
    with some funcs
    '''
    name = None
    value = None 

    def area(self):
        ''' raises Exception with msg '''
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        ''' validate intager vale entered'''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
