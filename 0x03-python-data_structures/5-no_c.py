#!/usr/bin/python3
def no_c(my_string):
    characater = "Cc"
    my_string = ''.join(x for x in my_string if x not in characater)
    return my_string
