#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0, None
    return len(sentence), sentence[0]
