#!/usr/bin/python3


def add_attribute(obj, atr, value):
    if type(obj) in (list, dict, set, str, int):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
