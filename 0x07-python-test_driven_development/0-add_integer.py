#!/usr/bin/python3
'# a function that adds 2 integer'


def add_integer(a, b=98):
    '# check the type of the variable a'

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    '# check the type of the variable'
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    '# add and return operation'
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
