def safe_print_list(my_list=[], x=0):
    cntr = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            cntr += 1
        except Exception as err:
            pass
    print()
    return (cntr)
