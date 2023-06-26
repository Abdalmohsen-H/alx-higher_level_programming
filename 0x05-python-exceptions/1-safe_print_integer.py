#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    # except Exception as err:
    except (TypeError, ValueError):
        # print(f"Unexpected {err=}, {type(err)=}")
        return False
