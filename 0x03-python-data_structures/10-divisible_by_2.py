#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    newlist = []
    for num in my_list:
        newlist.append(True if num % 2 == 0 else False)
    return newlist
