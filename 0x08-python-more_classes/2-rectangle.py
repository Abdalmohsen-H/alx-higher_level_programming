#!/usr/bin/python3
''' this is a module for a class
for rectangle task 2
A. Hesham
'''


class Rectangle:
    ''' This is a Rectangle class
    task 1
    '''
    def __init__(self, width=0, height=0):
        ''' intialize instance (object) of class
        Rectangle
        doc description for intialization function
        
        '''
        self.width = 0
        self.height = 0

    @property
    def width(self):
        '''width getter
        doc description for function
        '''
        return self.__width

    @width.setter
    def width(self, value):
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' instance method to
        return are of rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' instance method to return
        perimeter of regtangle (mo7eet)
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
