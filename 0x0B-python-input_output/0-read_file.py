#!/usr/bin/python3
'# a function that reads a text file (UTF8)'


def read_file(filename=""):
    '# read filei'

    with open(filename) as f:
        print(f.read(), end="")
