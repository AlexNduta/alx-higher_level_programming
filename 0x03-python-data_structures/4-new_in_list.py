#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    copied_list = my_list.copy()
    if my_list != []:
        if idx < 0 or idx >= length:
            return copied_list
        else:
            copied_list[idx] = element
            return copied_list
