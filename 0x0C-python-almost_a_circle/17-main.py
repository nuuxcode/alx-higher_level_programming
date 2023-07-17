#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    print(type(r1_dictionary))
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

    r4 = Square(2, 0, 7)
    r4_dictionary = r4.to_dictionary()
    print(type(r4_dictionary))
    r5 = Square.create(**r4_dictionary)
    print(r4)
    print(r5)
    print(r4 is r5)
    print(r4 == r5)
# square  :
# size, x=0, y=0, id=None
# rectangle :
# width, height, x=0, y=0, id=None
