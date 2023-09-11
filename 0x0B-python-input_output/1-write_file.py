#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ func """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
