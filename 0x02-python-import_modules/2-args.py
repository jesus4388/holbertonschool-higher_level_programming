#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 1:
    print(f"0 arguments.")
elif n == 2:
    print(f"1 argument:")
else:
    print(f"{n - 1} arguments:")
for i in range(1, n):
    print(f"{i}: {sys.argv[i]}")
