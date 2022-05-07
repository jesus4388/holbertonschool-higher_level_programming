#!/usr/bin/python3
def roman_to_int(roman_string):
    b = 0
    a = 0
    roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return 0
    for j in roman_string:
        for i in roma:
            if i == j:
                if a < roma.get(i):
                    b = b - (a*2)
                b = b + roma.get(i)
                a = roma.get(i)
    return b
