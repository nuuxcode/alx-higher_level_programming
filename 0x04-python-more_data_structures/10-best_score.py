#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return list(dict(sorted(a_dictionary.items(), key=lambda x: (-x[1], x[0]))))[0]
