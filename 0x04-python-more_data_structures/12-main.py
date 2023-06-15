#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "I"
print("{} 1 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "III"
print("{} 3 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} 21 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} 4 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIV"
print("{} 124 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "89"
print("{} 0 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} 0 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIX"
print("{} 99 = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXIX"
print("{} 89 = {}".format(roman_number, roman_to_int(roman_number)))
