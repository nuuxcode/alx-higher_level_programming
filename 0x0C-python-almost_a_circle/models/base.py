#!/usr/bin/python3
""" module doc """


class Base:
    """ class doc """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
