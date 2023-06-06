#!/usr/bin/python3
def islower(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return False
    elif ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
