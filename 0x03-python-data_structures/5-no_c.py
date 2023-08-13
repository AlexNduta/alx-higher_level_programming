#!/usr/bin/python3

def no_c(my_string):
    if my_string != []:
        clean_string = my_string.replace("c", "").replace("C", "")
        return clean_string
