#!/usr/bin/python3
'# a function that writes a string to a text file(UTF8)'


def write_file(filename="", text=""):
    '# write text in filename'

    with open(filename, "w") as f:
        f.write(text)
    return len(text)
