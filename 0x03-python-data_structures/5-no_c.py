#!/usr/bin/python3
# task 5 code


def no_c(my_string):
    tmplst = []
    for char in my_string:
        if char not in ('c', 'C'):
            tmplst.append(char)
            # print(char, end="")
    my_string = ''.join(tmplst)
    return my_string


# print(no_c(my_string))
