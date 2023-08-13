#!/bin/bash/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    cp = my_list.copy()
    if my_list:
        if idx < 0:
            return cp
        elif idx >= length:
            return my_list
        else:
            chgd = cp[idx] = element
            return chgd
