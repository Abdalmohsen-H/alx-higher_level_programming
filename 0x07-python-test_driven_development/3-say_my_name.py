#!/usr/bin/python3
''' task 2 on tdd project, print full name'''


def say_my_name(first_name, last_name=""):
    ''' a. Hesham task 1 on tdd , print full name
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
