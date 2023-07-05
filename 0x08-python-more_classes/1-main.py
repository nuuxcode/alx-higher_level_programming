#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle


try:
    myrectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    myrectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    myrectangle =  Rectangle(2, 3)
    myrectangle.width = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    myrectangle = Rectangle(2, 3)
    myrectangle.width = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    myrectangle =  Rectangle(2, 3)
    myrectangle.height = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    myrectangle = Rectangle(2, 3)
    myrectangle.height = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

myrectangle = Rectangle(2, 4)
print(sorted(myrectangle.__dict__))

myrectangle = Rectangle(2, 4)
print(myrectangle.width)




