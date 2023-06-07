#!/usr/bin/python3
# my solution for this advanced task
def magic_calculation(a, b, c):
    if (a < b):
        return c
    elif (c > b):
        return a + b
    else:
        return a * b - c


# python3 -c "import dis; dis.dis(open('102-magic_calculation.py').read())"
