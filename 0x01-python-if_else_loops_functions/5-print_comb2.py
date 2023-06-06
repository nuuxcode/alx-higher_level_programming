#!/usr/bin/python3
for num in range(0, 100):
    between = ", "
    if num == 99:
        between = ""
    print("{:02d}".format(num),end = between)
