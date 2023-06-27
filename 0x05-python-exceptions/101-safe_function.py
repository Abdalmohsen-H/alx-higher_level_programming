#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''
    this for task 8 -> file 101*
    about excute a function and if error print in stderr
    while return result else None
    '''
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
