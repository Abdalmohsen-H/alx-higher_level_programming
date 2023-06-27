#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''
    task 7 -> file 100*
    print err in stderr
    A.Hesham
    '''
    try:
        print("{:d}".format(value))
        return (True)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        # print("sys.exc_info(): {}".format(sys.exc_info()))
        return (False)
