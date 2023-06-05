#!/usr/bin/python3
# function for magic calc.
# use python3 -c
# import dis; dis.dis(open('102-magic_calculation.py').read())
# for testing in bash
def magic_calculation(a, b):
    # identation use 4 spaces for pystyle !
    return (98 + a ** b)
# explanation order was 98 is a const and a, b inputs
# "or local vars" no operation before
# because power should be done before addition
# also power require the a,b load first
# as they will be used then the additioni
