#!/usr/bin/python3
''' a module that read file and search
each line for a specific word
if line have the word, then
insert a specific line after
'''


def append_after(filename="", search_string="", new_string=""):
    ''' a function that read file and search
    each line for a specific word
    if line have the word, then
    insert a specific line after
    '''
    newtxt = []
    with open(filename, mode="r+") as file:
        # load lines to list
        lines = file.readlines()
        for line in lines:
            print(f"line: {line}")
            newtxt.append(line)
            # if found match
            if search_string in line:
                # add new string line after match line
                newtxt.append(new_string)
        file.seek(0)  # reset cursor to start of file
        file.writelines(newtxt)  # overwrite txt file
