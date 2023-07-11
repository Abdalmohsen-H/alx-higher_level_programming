#!/usr/bin/python3
''' a module that have a function
for writing to a file with utf-8 encoding
'''


def write_file(filename="", text=""):
    ''' function to write to a file '''
    if len(filename) > 0:
        mode = "w"
        with open(filename, mode, encoding="utf-8") as file:
            return file.write(text)
