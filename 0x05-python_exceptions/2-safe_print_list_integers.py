#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for item in range(x):
        try:
            print("{:d}".format[item], end='')
            y += 1
        except (TypeError, IndexError):
            continue
    print()
    return y
