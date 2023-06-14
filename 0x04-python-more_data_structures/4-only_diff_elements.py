#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1:
        return []
    return set_1.union(set_2)
