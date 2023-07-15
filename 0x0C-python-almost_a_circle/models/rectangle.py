#!/usr/bin/python3
""" module doc """
from models.base import Base


class Rectangle(Base):
    """ class doc """

    def check_int(self, attr, val):
        if not isinstance(val, int):
            raise TypeError(f"{attr} must be an integer")

    def check_positive(self, attr, val):
        if val <= 0:
            raise ValueError(f"{attr} must be > 0")

    def check_positive_zero(self, attr, val):
        if val < 0:
            raise ValueError(f"{attr} must be >= 0")

    def checks(self, width, height, x, y):
        self.check_int("width", width)
        self.check_int("height", height)
        self.check_int("x", x)
        self.check_int("y", y)
        self.check_positive("width", width)
        self.check_positive("height", height)
        self.check_positive_zero("x", x)
        self.check_positive_zero("y", y)

    def __init__(self, width, height, x=0, y=0, id=None):
        self.checks(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.check_int("width", val)
        self.check_positive("width", val)
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.check_int("height", val)
        self.check_positive("height", val)
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.check_int("x", val)
        self.check_positive_zero("x", val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.check_int("y", val)
        self.check_positive_zero("y", val)
        self.__y = val
