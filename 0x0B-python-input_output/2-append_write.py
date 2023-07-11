#!/usr/bin/python3
''' a module that have a function
for append text to a file with utf-8 encoding
'''


def append_write(filename="", text=""):
    ''' function to append text to a file '''
    if len(filename) > 0:
        mode = "a"
        with open(filename, mode, encoding="utf-8") as file:
            return file.write(text)
