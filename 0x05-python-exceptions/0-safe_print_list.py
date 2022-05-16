#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    b = 0
    for lo in range(0, x):
        try:
            print("{}".format(my_list[lo]), end="")
            b = b + 1
        except IndexError:
            break
    print()
    return (b)
