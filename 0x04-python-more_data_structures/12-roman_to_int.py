#!/usr/bin/python3
def roman_to_int(roman_string):
    b = 0
    I = 0
    V = 0
    X = 0
    L = 0
    C = 0
    D = 0
    c = 0
    a = 0
    if roman_string == None:
        return 0
    if roman_string:
        for i in roman_string:
            if i == 'I':
                c = 1
                a = 1
            if i == 'V':
                c = 5
            if i == 'X':
                c = 10
            if i == 'L':
                c = 50
            if i == 'C':
                c = 100
            if i == 'D':
                c = 500 
            if  a == 1 and c > 1:
                b = b + c - 2
                a = 0
            else:
                b = b + c
    else:
        return 0
    return b
