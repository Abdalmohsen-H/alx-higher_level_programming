#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        # except Exception as err:
        # print(f"Unexpected {err=}, {type(err)=}")
        return (False)
