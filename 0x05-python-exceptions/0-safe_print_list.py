#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for ele in my_list:
            if (counter >= x):
                break
            print("{}".format(ele), end="")
            counter += 1
        print("".format())
        return counter
    except ValueError:
        print("ValueError error")
