#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        res = 0
        if argv[2] == '+':
            res = add(a, b)
        elif argv[2] == '-':
            res = sub(a, b)
        elif argv[2] == '*':
            res = mul(a, b)
        elif argv[2] == '/':
            res = div(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, res))
