#!/usr/bin/python3
""" check if inherited """


def inherits_from(obj, a_class):
    """ subclass find """
    return isinstance(obj, a_class) and not type(obj) is a_class
