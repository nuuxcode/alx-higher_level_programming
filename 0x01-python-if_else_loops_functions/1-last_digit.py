#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if last_digit == 0:
    second_string = f"and is 0"
if last_digit < 6:
    second_string = f"and is less than 6 and not 0"
if last_digit > 5:
    second_string = f"and is greater than 5"
print(f"Last digit of {number:d} is {last_digit:d} {second_string}")