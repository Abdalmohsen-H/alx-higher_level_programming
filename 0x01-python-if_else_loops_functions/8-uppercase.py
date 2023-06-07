#!/usr/bin/python3
case_alt_diff = 32


def uppercase(str):
    for char in str:
        if 96 < ord(char) < 127:  # only change lower case chars
            finchar = ord(char) - case_alt_diff
        else:
            finchar = ord(char)
        print("{}".format(chr(finchar)), end="")

    print("{}".format(""))


# uppercase("test small")
# uppercase("Best School 98 Battery street")
