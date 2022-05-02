#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    a = len(my_list) - 1
    if idx > a:
        return None
    for i in my_list:
        if idx == i:
            return a
