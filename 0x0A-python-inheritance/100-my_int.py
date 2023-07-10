#!/usr/bin/python3
''' a module that have a class inherits int
Task 11 : A. Hesham
'''


class MyInt(int):
    ''' have  equal and not equal operated
    inverted than one used on int
    '''
    def __init__(self, value):
        ''' intialize the instance '''
        self.value = value

    def __ne__(self, other):
        ''' act in reversed way than not equal'''
        if self.value != other:
            return False
        else:
            return True

    def __eq__(self, other):
        ''' act in opposite way than equal'''
        if self.value != other:
            return True
        else:
            return False
