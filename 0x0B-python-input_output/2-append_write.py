#!/usr/bin/python3
"""
Module 2-read_lines

fnction that appends a string
"""


def append_write(filename="", text=""):
    """returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
