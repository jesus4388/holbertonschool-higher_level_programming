#!/usr/bin/python3
'# a function that appends a string at the end of a text file'


def append_write(filename="", text=""):
    '# appends a string at the end of a text'

    with open(filename, "a") as f:
        f.write(text)
    return len(text)
