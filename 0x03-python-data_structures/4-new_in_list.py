#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list) - 1
    copy = my_list[:]
    if idx > size:
        return copy
    if idx < 0:
        return copy
    copy[idx] = element
    return copy
