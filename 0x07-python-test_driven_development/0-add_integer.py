#!/usr/bin/python3
""" This is a function that takes two parameters and adds the
    two numbers"""


def add_integer(a, b=98):
    """returns a sum of a and b typcasted to integers """
    if not isinstance(a, (float, int)):
        raise TyperError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TyperError("b must be an integer")
    return int(a) + int(b)
