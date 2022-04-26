#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    if number % 10 in range(6, 10):
        print(f"Last digit of -{number} is {number % 10} and is greater than 5")
    elif number % 10 == 0:
        print(f"Last digit of -{number} is {number % 10} and is 0")
    elif number % 10 in range(1, 6):
        print(f"Last digit of -{number} is {number % 10} and is less than 6 and not 0")
elif number > 0:
    if number % 10 in range(6, 10):
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
    elif number % 10 == 0:
        print(f"Last digit of {number} is {number % 10} and is 0")
    elif number % 10 in range(1, 6):
    	print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
