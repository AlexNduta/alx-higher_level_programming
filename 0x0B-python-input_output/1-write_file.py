#!/usr/bin/python3
""" this is the 'write_file'
    the function takes the filename an the contents to be written to the file
    the function later on rerturns the number of characters written to the file
"""


def write_file(filename="", text=""):
    """ open the file so as to read read its content """
    with open(filename, 'w') as file:
        reading_writting = file.write(text)
        return reading_writting
