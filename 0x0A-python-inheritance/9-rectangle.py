#!/usr/bin/python3
''' a module that have a class inherits other
class
Task 9 : A. Hesham
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' rectangle class inherits
    base geometery
    '''
    def __init__(self, width, height):
        ''' intialize the object for this class '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        ''' repr for str() and print() '''
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        ''' override inherited area ()'''
        return self.__width * self.__height
