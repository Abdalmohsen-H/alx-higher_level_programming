#!/usr/bin/python3
''' a module that have a class inherits other
class
Task 8 : A. Hesham
'''


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
