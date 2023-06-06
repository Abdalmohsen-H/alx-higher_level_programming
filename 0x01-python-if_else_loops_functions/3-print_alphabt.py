#!/usr/bin/python3
for asciichar in range(ord('a'), ord('z')+1):
    if asciichar not in (101, 113):  # ascii 113 = q , 101 = e
        print(chr(asciichar), end='')
