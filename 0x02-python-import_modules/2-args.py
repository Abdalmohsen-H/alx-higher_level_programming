#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} ".format(len(argv)-1), end="")
    if len(argv) == 2:
        print("argument:")
    elif len(argv) == 1:
        print("arguments.")
    else:
        print("arguments:")
    for arg in range(1, len(argv)):
        print("{}: {}".format(arg, argv[arg]))
