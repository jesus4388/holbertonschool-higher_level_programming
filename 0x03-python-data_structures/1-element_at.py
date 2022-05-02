#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list) - 1
    if idx < 0:
        return None
    if idx > a:
        return None
    for i in my_list:
        if i == idx + 1:
            return i
