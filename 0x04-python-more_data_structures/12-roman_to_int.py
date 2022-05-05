#!/usr/bin/python3
def roman_to_int(roman_string):
    b = 0
    V = 0
    X = 0
    L = 0
    C = 0
    D = 0
    c = 0
    a = 1
    M = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    if roman_string:
        for j in roman_string:
            if j == 'I':
                c = 1
            if j == 'V':
                c = 5
            if j == 'X':
                c = 10
            if j == 'L':
                c = 50
            if j == 'C':
                c = 100
            if j == 'D':
                c = 500
            if j == 'M':
                c = 1000
            if a < c:
                b = c - b
                a = c
            else:
                b = b + c
                if b > 1000:
                    b = 1000 - 10
    return b
