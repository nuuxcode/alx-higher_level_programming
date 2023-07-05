#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def height(self):
        return self.__height

    def __setattr__(self, name, value):
        if name == "width":
            self.width(value)
        elif name == "height":
            self.height(value)
        else:
            super().__setattr__(name, value)

    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def width(self):
        return self.__width

    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")
