#!/bin/python3
""" Defines a Sauare object"""


class Square:
    """ This class defines the property of the Square object
        Attributes:
            _size(int): this is the size of our square
    """
    def __init__(self, size):
        """Initialises a square
        Args: 
            size(int): This is the size of our square
        returns: None
        """
        self._size = size
