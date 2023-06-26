def safe_print_list(my_list=[], x=0):
    cntr = 0
    for itm in my_list:
        try:
            if cntr <= (x - 1):
                print(f"{itm}", end="")
                cntr += 1
        except Exception as err:
            pass
    print()
    return (cntr)
