#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
        """
        except Exception as err:
            print("err type -> {}".format(err))
        """
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(res))
    return res
