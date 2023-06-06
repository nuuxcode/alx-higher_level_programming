#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        newstring += str[i]
    return newstring
