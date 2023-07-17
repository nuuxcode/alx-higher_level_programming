#!/usr/bin/python3
""" module doc for rectangle """
from models.base import Base


class Rectangle(Base):
    """ class doc for rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ func doc """
        self.checks(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def check_int(self, attr, val):
        """ func doc """
        if not isinstance(val, int):
            raise TypeError(f"{attr} must be an integer")

    def check_positive(self, attr, val):
        """ func doc """
        if val <= 0:
            raise ValueError(f"{attr} must be > 0")

    def check_positive_zero(self, attr, val):
        """ func doc """
        if val < 0:
            raise ValueError(f"{attr} must be >= 0")

    def checks(self, width, height, x, y):
        """ func doc """
        self.check_int("width", width)
        self.check_int("height", height)
        self.check_int("x", x)
        self.check_int("y", y)
        self.check_positive("width", width)
        self.check_positive("height", height)
        self.check_positive_zero("x", x)
        self.check_positive_zero("y", y)

    def area(self):
        """ func doc """
        return self.__width * self.__height

    def display(self):
        """ func doc """
        string = ""
        for i in range(0, self.__height+self.__y):
            if self.__y > i:
                string += "\n"
                continue
            for j in range(0, self.__width+self.__x):
                if j >= self.__x:
                    string += "#"
                else:
                    string += " "
            if i == self.__height+self.__y-1:
                string += "\n"
                break
            string += "\n"
        print(string, end="")

    def __str__(self):
        """ func doc """
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ func doc """
        if len(args) == 0:
            id = kwargs["id"] if "id" in kwargs else self.id
            super().__init__(id)
            width = kwargs["width"] if "width" in kwargs else self.__width
            height = kwargs["height"] if "height" in kwargs else self.__height
            x = kwargs["x"] if "x" in kwargs else self.__x
            y = kwargs["y"] if "y" in kwargs else self.__y
        else:
            if len(args) >= 1:
                super().__init__(args[0])
            width = args[1] if len(args) >= 2 else self.__width
            height = args[2] if len(args) >= 3 else self.__height
            x = args[3] if len(args) >= 4 else self.__x
            y = args[4] if len(args) >= 5 else self.__y
        self.checks(width, height, x, y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """ func doc """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """ func doc """
        return self.__width

    @width.setter
    def width(self, val):
        """ func doc """
        self.check_int("width", val)
        self.check_positive("width", val)
        self.__width = val

    @property
    def height(self):
        """ func doc """
        return self.__height

    @height.setter
    def height(self, val):
        """ func doc """
        self.check_int("height", val)
        self.check_positive("height", val)
        self.__height = val

    @property
    def x(self):
        """ func doc """
        return self.__x

    @x.setter
    def x(self, val):
        """ func doc """
        self.check_int("x", val)
        self.check_positive_zero("x", val)
        self.__x = val

    @property
    def y(self):
        """ func doc """
        return self.__y

    @y.setter
    def y(self, val):
        """ func doc """
        self.check_int("y", val)
        self.check_positive_zero("y", val)
        self.__y = val
