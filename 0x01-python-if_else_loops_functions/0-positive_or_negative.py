#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive\n")  # number is positive
elif number == 0:
    print(f"{number:d} is zero\n")  # number is zero
else:
    print(f"{number:d} is negative\n")  # number is negative
