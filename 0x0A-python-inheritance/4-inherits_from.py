#!/usr/bin/python3
''' a module that have a function
that takes an (object or a class) &
another class as 2nd input
Task 4 : A. Hesham
returns True if 1st input's class is inheriting
(directly or indirectly) fro_m the specified class
else false
'''


def inherits_from(obj, a_class):
    ''' a function that checks if object's class
    inheriting (directly or indirectly)
    fro_m the specified class
    return True or False
    '''
    # Another solutions:

    # return issubclass(obj.__class__, a_class)\
    # and (a_class != type(obj))

    # return isinstance(obj, a_class) and (a_class != type(obj))

    # return (a_class in list(type(obj).__mro__)\
    #        and (a_class != type(obj)))

    # return issubclass(type(obj), a_class) and (a_class != type(obj))

    if (a_class == type(obj)):  # if oject is an instance of a_class
        return False
    else:  # then check if obj's class inheriting fro-m a_clas
        # below line returns True if obj's class inherit fr.om a_class
        return issubclass(type(obj), a_class)
