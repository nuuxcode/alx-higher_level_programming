#!/usr/bin/python3
""" module doc """
from models.base import Base


class Rectangle(Base):
    """ class doc """

    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val


'''
    def get_width(self):
        return self.__width

    def set_width(self, val):
        self.__width = val

    def get_height(self):
        return self.__height

    def set_height(self, val):
        self.__height = val

    def get_x(self):
        return self.__x

    def set_x(self, val):
        self.__x = val

    def get_y(self):
        return self.__y

    def set_y(self, val):
        self.__y = val
'''
