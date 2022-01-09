#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    for item in my_list:
        if len(my_list) == 0:
            return None
        elif item > maximum:
            maximum = item
    return maximum
