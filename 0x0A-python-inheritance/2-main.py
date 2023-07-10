#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = True
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, bool):
    print("{} is an instance of the class {}".format(a, bool.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
