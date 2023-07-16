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
