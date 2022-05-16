#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        val = True
    except ValueError:
        val = False
    return val
