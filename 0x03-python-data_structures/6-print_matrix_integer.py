#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for ele2 in ele:
            print("{:d}".format(ele2),
                  end="" if ele[len(ele)-1] == ele2 else " ")
        print("".format())
