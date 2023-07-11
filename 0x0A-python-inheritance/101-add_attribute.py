#!/usr/bin/python3
""" module """


def add_attribute(obj, atr, value):
    """function """
    if type(obj) in (list, dict, set, str, int, float, complex, frozenset):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
