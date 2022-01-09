#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            l = 1
            for item in row:
                if l == len(row):
                    print("{:d}".format(item), end="")
                else:
                    print("{:d}".format(item), end=" ")
                l = l + 1
            print()

