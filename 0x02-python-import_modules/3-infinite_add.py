#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    if len(argv) == 1:
        print("{}".format(sum))
    else:
        for arg in range(1, len(argv)):
            sum += int(argv[arg])
        print("{}".format(sum))
