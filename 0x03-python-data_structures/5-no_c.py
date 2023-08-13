#!/usr/bin/python3

def no_c(my_string):
    if my_string != []:
        table = str.maketrans({"C":"", "c":""})
        cleaned_string = my_string.translate(table)
        return cleaned_string
