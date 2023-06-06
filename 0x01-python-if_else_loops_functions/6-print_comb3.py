#!/usr/bin/python3
for frst in range(10):
    for scnd in range(frst+1, 10):
        if frst == 8 and scnd == 9:
            # -print("89")
            print("{}".format(89))
        else:
            # print-(f"{frst}{scnd}", end=", ")
            print("{}{}".format(frst, scnd), end=", ")
