#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if(num >= 97 and num < 123):
            num = num - 32
            i = chr(num)
        print(f"{i}", end="")
    print("")
