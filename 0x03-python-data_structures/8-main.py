#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
length, first = multiple_returns(None)
print("Length: {:d} - First character: {}".format(length, first))
length, first = multiple_returns("")
print("Length: {:d} - First character: {}".format(length, first))
length, first = multiple_returns("a")
print("Length: {:d} - First character: {}".format(length, first))
