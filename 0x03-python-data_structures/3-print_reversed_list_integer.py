#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == 0:
        return None
    for i in my_list[::-1]:
        print("{}".format(i))
