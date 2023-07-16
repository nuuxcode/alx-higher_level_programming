#!/usr/bin/python3
""" module doc """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class doc """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) \
{self.x}/{self.y} {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.check_int("width", val)
        self.check_positive("width", val)
        self.width = val

    def update(self, *args, **kwargs):
        if len(args) == 0:
            id = kwargs["id"] if "id" in kwargs else self.id
            self.id = id
            size = kwargs["size"] if "size" in kwargs else self.width
            x = kwargs["x"] if "x" in kwargs else self.x
            y = kwargs["y"] if "y" in kwargs else self.y
        else:
            if len(args) >= 1:
                self.id = args[0]
            size = args[1] if len(args) >= 2 else self.width
            x = args[2] if len(args) >= 4 else self.x
            y = args[3] if len(args) >= 5 else self.y
        self.checks(size, size, x, y)
        self.width = size
        self.x = x
        self.y = y

        def to_dictionary(self):
            return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
