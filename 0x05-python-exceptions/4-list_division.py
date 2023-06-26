#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nwlst = []
    for idx in range(list_length):
        res = 0  # this line must be 1st line inside for loop
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            nwlst.append(res)
    return nwlst
