#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -number % 10
    last_digit *= -1
else:
    last_digit = number % 10
if last_digit == 0:
    second_string = f"and is 0"
elif last_digit < 6:
    second_string = f"and is less than 6 and not 0"
elif last_digit > 5:
    second_string = f"and is greater than 5"
print(f"Last digit of {number:d} is {last_digit:d} {second_string}")
