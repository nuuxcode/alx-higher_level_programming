#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, "counter", 0) + 1
    return ', '.join('BestSchool' for _ in range(magic_string.counter))
