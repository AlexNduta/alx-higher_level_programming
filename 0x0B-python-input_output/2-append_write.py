#!/usr/bin/python3
""" this is the funcition 'append_write'
    this function intends on writting to our file and incase
    the filen does not exist it is created afresh
"""
def append_write(filename="", text=""):
    """opening the file enables us to make any operations on out file.
        in this case, we will be appening to our file if it exist
    """
    with open(filename, 'a') as  file:
        appending_to_file = file.write(text)
        return appending_to_file
