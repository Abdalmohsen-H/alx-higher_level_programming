#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:  # handle nagtive n index
        n = len(str) + n
    return (str[:n] + str[n+1:])


# remove_char_at("test", 2)
# remove_char_at("Chicago", -3)
