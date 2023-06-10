#!/usr/bin/python3
def check_tuple(tuple=()):
    lent = len(tuple)
    if lent == 0:
        return 0, 0
    if lent == 1:
        tuple += 0,
        return tuple
    if lent >= 2:
        return tuple[0], tuple[1]


def add_tuple(tuple_a=(), tuple_b=()):
    a = check_tuple(tuple_a)
    b = check_tuple(tuple_b)
    return a[0]+b[0], a[1]+b[1]
