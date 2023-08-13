#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    copied_list = my_list.copy()
    if idx < 0:
        return cp
    elif idx >= length:
        return my_list
    else:
        copied_list[idx] = element
        return copied_list
