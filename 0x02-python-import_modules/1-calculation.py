#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5
print(f"{a} + {b} = {add(a, b)}")

if __name__ == "__main__":
    from calculator_1 import sub
    a = 10
    b = 5
print(f"{a} - {b} = {sub(a, b)}")

if __name__ == "__main__":
    from calculator_1 import mul
    a = 10
    b = 5
print(f"{a} * {b} = {mul(a, b)}")

if __name__ == "__main__":
    from calculator_1 import div
    a = 10
    b = 5
print(f"{a} / {b} = {div(a, b)}")
