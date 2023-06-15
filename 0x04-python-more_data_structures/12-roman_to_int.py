#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if roman_string is not None:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        for char in roman_string:
            if char in roman:
                sum += roman[char]
    return sum
