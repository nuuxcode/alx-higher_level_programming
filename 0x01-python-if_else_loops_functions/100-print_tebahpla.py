#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for i in str:
        if 'a' <= i <= 'z':
            newstring += chr((ord(i) - ord('a')) + ord('A'))
        else:
            newstring += i
    return newstring


for alpha in range(ord('z'), ord('a')+-1, -1):
    if alpha % 2 == 1:
        alpha = ord(uppercase(chr(alpha)))
    print("{}".format(chr(alpha)), end='')
