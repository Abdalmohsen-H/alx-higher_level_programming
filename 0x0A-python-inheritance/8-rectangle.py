#!/usr/bin/python3
''' a module that have an empty class
Task 8 : A. Hesham
'''


class Rectangle(BaseGeometry):
    ''' rectangle class inherits from
    base geometery
    '''
    def __init__(self, width, height):
        ''' intialize the object from this class '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
