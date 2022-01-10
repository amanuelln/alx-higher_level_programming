#!/usr/bin/python3
def no_c(my_string):
    res = []
    for item in my_string:
        if item != 'c' and item != 'C':
            res.append(item)
    return "".join(res)
