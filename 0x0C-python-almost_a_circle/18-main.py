#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]
    #print(list_rectangles_input)
    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()
    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")
# square  :
# size, x=0, y=0, id=None
# rectangle :
# width, height, x=0, y=0, id=None
    s1 = Square(5)
    #print(s1.__dict__)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    #print(list_squares_input[0].__dict__,list_squares_input[1].__dict__)
    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
