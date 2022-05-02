#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    for i in my_list:
        if i > a:
            a = i
    if a == 0:
        return None
    else:
        return a
