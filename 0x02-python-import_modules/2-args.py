#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)
    if len == 1:
        print("0 arguments.")
    elif len > 1:
        print("{:d} argument{:s}".format(len-1, "s:" if len > 2 else ":"))
        for i in range(1, len):
            print("{:d}: {:s}".format(i, argv[i]))
