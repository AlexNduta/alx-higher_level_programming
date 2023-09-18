#!/usr/bin/python3
""" This is the 'Base' class implementation"""


class Base:
    """our function contains a  private class attribute '__nb_objects'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ create a class constructor
            attributes: id=
            if id is none then we stick to it, esle we increment the class attr
            and assign it to the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
