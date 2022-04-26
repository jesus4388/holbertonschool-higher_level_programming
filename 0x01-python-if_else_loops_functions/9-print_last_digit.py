#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = number * -1
        num = number % 10
        print(f"{number % 10}", end="")
    else:
        print(f"{number % 10}", end="")
        num = number % 10
    return num
