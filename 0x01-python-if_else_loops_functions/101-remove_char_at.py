#!/usr/bin/python3
def remove_char_at(str, n):
    '''
    # python string indexing accept negative
    if n < 0:
        n = len(str) + n
    '''
    # c string indexing way
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])


# remove_char_at("tset", 2)
# remove_char_at("Chicago", -3)
