#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """class"""
    def __new__(cls, num):
        return super().__new__(cls, num)

    def __init__(self, num):
        self.num = num

    def __eq__(self, num2):
        return self.num != num2

    def __ne__(self, num2):
        return self.num == num2
