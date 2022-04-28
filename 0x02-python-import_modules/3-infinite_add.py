#!/usr/bin/python3
import sys
add = 0
if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n == 1:
        print(f"0")
    for i in range(1, n):
        if (int(sys.argv[i]) >= 0 and int(sys.argv[i]) <= 9):
            add += int(sys.argv[i])
    print(f"{add}")
