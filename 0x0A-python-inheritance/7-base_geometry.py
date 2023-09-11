#!/usr/bin/python3
""" geometry module """


class BaseGeometry:
    """getmetry class"""
    pass

    def area(self):
        """ the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validation """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
