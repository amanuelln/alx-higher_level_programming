#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 1
        for item in row:
            if count == len(row):
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
            count = count + 1
        print()
