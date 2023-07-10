#!/usr/bin/python3
''' a module that have a class inherits
list
Task 1 : A. Hesham
with public func
'''


class MyList(list):
    ''' class has a function that
    prints sorted list
    A. Hesham
    '''

    def print_sorted(self):
        ''' pub func that prints sorted list '''
        print(sorted(list(self)))
