#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for i in range(0, len(str)):
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            newstring += chr((ord(str[i]) - ord('a')) + ord('A'))
        else:
            newstring += chr(ord(str[i]))
    print("{}".format(newstring))
