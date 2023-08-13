#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    replaced = my_list.insert(idx, element)
    if idx < 0 or idx >= length:
        return my_list
    else:
       return replaced
