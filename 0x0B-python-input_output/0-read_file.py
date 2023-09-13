#!/usr/bin/python2
"""
Module 0-read_file

A function that reads text file and prints it to stdout
"""


def read_file(filename=""):
    """ our function takes in the name of the file as a parameter"""
    with open(filename,'r', encoding="utf-8") as bs:
        print(bs.read(), end="")
