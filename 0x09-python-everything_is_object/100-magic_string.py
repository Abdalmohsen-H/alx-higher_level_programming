#!/usr/bin/python3
def magic_string():
    magic_string.ctr = getattr(magic_string, 'ctr', 0) + 1
    return ('BestSchool, ' * (magic_string.ctr - 1)) + 'BestSchool'
