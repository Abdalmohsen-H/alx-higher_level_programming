#!/usr/bin/python3
# Print alphabet reversed and alternating upper and lower case
# i.e. zYxWvUtSr ... bA
asciichar = 122
case_alt_diff = 0
while (asciichar > 96):  # till reaching a
    # 122 to 97 ascii for z to a
    print("{}".format(chr(asciichar - case_alt_diff)), end='')
    asciichar -= 1  # decrement ascii to revese alpha
    case_alt_diff = 32 if (not case_alt_diff) else 0  # case change
