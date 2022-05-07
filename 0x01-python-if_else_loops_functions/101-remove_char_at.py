#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    count = 0
    if n < 0 or n > len(str):
        return(f"{str}")
    for i in str:
        if count != n:
            copy = copy + i
        count = count + 1
    return copy
