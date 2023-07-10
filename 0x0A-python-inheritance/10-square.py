#!/usr/bin/python3
''' a module that have a class inherits Rectangle
Task 10 : A. Hesham
'''


BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    ''' rectangle class inherits
    base geometery
    '''
    def __init__(self, size):
        ''' intialize the object for this class '''
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' override inherited area ()'''
        return self.__size * self.__size

    def __repr__(self):
        ''' repr for str() and print() '''
        return f"[{Rectangle.__name__}] {self.__size}/{self.__size}"
