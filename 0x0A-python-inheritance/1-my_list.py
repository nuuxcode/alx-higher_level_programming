#!/usr/bin/python3
"""
    prints listsorted
"""


class MyList(list):
    """
    sort function
    """

    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
