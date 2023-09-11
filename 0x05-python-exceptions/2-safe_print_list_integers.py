#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    counter2 = 0
    for ele in my_list:
        try:
            if (counter >= x):
                break
            print("{:d}".format(ele), end="")
            counter += 1
        except (ValueError, TypeError):
            counter2 += 1
    if (counter+counter2 < x):
        raise IndexError("list index out of range")
    print("".format())
    return counter
