#!/usr/bin/python3
import sys
add = 0
addr = 0
if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n == 0:
        print(f"0")
    for i in range(1, n):
        if (int(sys.argv[i]) < 0):
            add -= int(sys.argv[i])
        if (int(sys.argv[i]) > 0):
            addr += int(sys.argv[i])
    add = add - addr
    print(f"{add}")
