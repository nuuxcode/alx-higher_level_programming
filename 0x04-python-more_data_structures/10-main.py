#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

my_dict = { }
best_key = best_score(my_dict)
print("Best: {}".format(best_key))
