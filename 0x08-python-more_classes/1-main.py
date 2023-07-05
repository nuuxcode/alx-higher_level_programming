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

myrectangle = Rectangle(2, 4)
print(myrectangle.height)

myrectangle = Rectangle(4)
print("{} - {}".format(myrectangle.width, myrectangle.height))

myrectangle = Rectangle()
print("{} - {}".format(myrectangle.width, myrectangle.height))

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.width = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.height = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))

try:
    myrectangle = Rectangle(2, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    myrectangle = Rectangle("2", "2")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))


