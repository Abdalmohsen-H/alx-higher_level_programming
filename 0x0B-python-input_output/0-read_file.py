#!/usr/bin/python3
''' a module that have a function
for reading a file with utf-8 encoding
'''


def read_file(filename=""):
    ''' function to read file '''
    if len(filename) > 0:
        mode = "r"  # optional
        with open(filename, mode, encoding="utf-8") as file:
            for lines in file:  # end="" to avid add \n via print
                print(lines, end="")  # dont forget end
