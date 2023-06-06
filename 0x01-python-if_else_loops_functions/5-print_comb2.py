#!/usr/bin/python3
for num in range(0, 99):
    # pri-nt(f'{num:02d}', end=", ")  # {num:02d} to use two digits
    print("{:02d}".format(num), end=", ")
print("{}".format(99))  # to have newline after 99
