#!/usr/bin/python2
""" A function that reads text file and prints it to stdout"""


def read_file(filename=""):
    """ our function takes in the name of the file as a parameter"""
    with open(filename, encoding="utf-8") as bs:
        reading = bs.read()
        print(reading, end="")
