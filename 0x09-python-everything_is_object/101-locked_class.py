#!/usr/bin/python3
'''
this a locked class that doesn't any
instance attributes except specific attribute
'''


class LockedClass:
    ''' this class doesn't have any attributes except specified
    and have restriction conditions
    __slots__ only accept squence like lists or tuples ...
    '''

    __slots__ = ["First_name"]
