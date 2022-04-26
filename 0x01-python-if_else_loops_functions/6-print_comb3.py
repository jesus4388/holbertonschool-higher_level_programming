#!/usr/bin/python3
for b in range(0, 9):
    for i in range(b + 1, 10):
        if not (b == 8 and i == 9):
            print("{}{}".format(b, i), end=", ")
        else:
            print("{}{}".format(b, i))
