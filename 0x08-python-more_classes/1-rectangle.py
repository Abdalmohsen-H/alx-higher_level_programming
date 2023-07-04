#!/usr/bin/python3
''' this is a module for a class
for rectangle task 1
A. Hesham
'''


class Rectangle:
    ''' This is a Rectangle class
    task 1
    '''
    def __init__(self, width=0, height=0):
        ''' intialize instance (object) of class
        Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width  getter
        doc description for function
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter
        doc description for function
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height  getter
        doc description for function
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter
        doc description for function
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("wheightidth must be >= 0")
        self.__height = value
