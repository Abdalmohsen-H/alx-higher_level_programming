#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
digit = (abs(number) % 10) * sign
if (digit > 5):
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif (digit < 6 and (digit)):  # to exclude digit == 0
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {digit} and is 0")
