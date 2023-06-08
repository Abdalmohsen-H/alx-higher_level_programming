#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    definednames = dir(hidden_4)  # names defined by a module
    definednames.sort()
    for definedname in definednames:
        if definedname[0] != "_":  # if_not started with _
            print("{}".format(definedname))
