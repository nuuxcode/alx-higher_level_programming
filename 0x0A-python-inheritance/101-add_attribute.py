#!/usr/bin/python3
""" module """


def add_attribute(obj, atr, value):
    """function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
