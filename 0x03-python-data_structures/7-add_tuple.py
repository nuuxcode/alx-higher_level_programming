#!/usr/bin/python3
def check_tuple(tuple=()):
    if len(tuple) == 0:
        return 0, 0
    if len(tuple) == 1:
        return tuple[0], 0
    return tuple


def add_tuple(tuple_a=(), tuple_b=()):
    a = check_tuple(tuple_a)
    b = check_tuple(tuple_b)
    return a[0]+b[0], a[1]+b[1]
