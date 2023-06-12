#!/usr/bin/python3
# task 8 code to return multiple values using tuple


def multiple_returns(sentence):
    # return two values, 1st strng length
    # 2nd value is the first char of input str
    # unless inpt str is empty then 2nd val will be None
    strnglength = len(sentence)
    if strnglength < 1:  # if string is empty
        return (strnglength, None)
    else:
        return (strnglength, sentence[0])
