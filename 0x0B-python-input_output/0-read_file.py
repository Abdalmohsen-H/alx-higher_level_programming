#!/usr/bin/python3
''' a module that have a function
for reading a file with utf-8 encoding
'''


def read_file(filename=""):
    ''' function to read file '''
    if len(filename) > 0:
        mode = "r"
        with open(filename, mode, encoding="utf-8") as file:
            for lines in file:
                print(lines, end="")
