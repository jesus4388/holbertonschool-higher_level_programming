#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        a = len(my_list)
        if (idx < 0 or idx > a):
            return my_list
        del my_list[idx]
        return my_list
    else:
        return None
