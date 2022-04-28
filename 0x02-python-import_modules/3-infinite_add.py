#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    add = 0
    i = 1
    if n == 2:
        print(f"{sys.argv[i]}")
    elif n > 2:
        for i in range(1, n):
            add += int(sys.argv[i])
        print(f"{add}")
    else:
        print('0')
