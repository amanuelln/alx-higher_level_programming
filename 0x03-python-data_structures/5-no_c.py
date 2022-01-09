#!/usr/bin/python3
def no_c(my_string):
    no_c_list = list(my_string)
    for i in no_c_list:
        if i == 'c' or i == 'C':
            no_c_list.remove(i)
            return "".join(no_c_list)
