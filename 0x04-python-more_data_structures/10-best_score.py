#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        return list(dict(sorted(a_dictionary.items(),
                                key=lambda x: (-x[1], x[0]))))[0]
