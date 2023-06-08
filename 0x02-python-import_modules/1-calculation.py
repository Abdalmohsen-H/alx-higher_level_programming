#!/usr/bin/python3
# import modules
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    # define vars
    a = 10
    b = 5
    # print output
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
