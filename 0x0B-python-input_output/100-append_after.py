#!/usr/bin/python3
''' a module that read file and search
each line for a specific word
if line have the word, then
insert a specific line after
'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r+") as file:
        donechars = 0
        for line in file:
            donechars += len(line)
            if search_string in line:
                file.seek(donechars, 0)  # move cursor after line
                file.write(new_string)
                donechars += len(new_string)
                file.seek(donechars, 0)
