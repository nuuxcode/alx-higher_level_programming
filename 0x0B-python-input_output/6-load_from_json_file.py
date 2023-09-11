#!/usr/bin/python3
""" module """
import json


def load_from_json_file(filename):
    """ func """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
