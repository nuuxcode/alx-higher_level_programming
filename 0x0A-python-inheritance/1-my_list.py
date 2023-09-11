#!/usr/bin/python3
"""
    prints listsorted
"""


class MyList(list):
    """
    sort function
    """

    def print_sorted(self):
        print(sorted(self))
