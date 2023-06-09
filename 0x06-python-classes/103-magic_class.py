#!/usr/bin/python3
"""
given bytecode .pyc I figured out the .py file
python code for circle calulations
"""


import math


class MagicClass:
    """ circle class """

    def __init__(self, radius=0):
        """ intialize circle instance"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ calculate area """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        circle circumference (moheet)
        """
        return (2 * math.pi * self.__radius)
