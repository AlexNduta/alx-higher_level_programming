#!/usr/bin/python3
"""Rectangle class"""


from .base import Base  # Import the base class


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes: width, height, x, y, and id."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width."""
        if isinstance(value, (int, float)):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be a number (int or float)")

    @height.setter
    def height(self, value):
        """Setter for height."""
        if isinstance(value, (int, float)):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be a number (int or float)")

    @x.setter
    def x(self, value):
        """Setter for x."""
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, value):
        """Setter for y."""
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ The area method, that returns the area of our rectangle"""
        return self.__width * self.__height

    def display(self):
        """ the display method that prints '#' as area representation"""
        disp = "#"
        for has in range(self.__height):
            print(disp * self.__width)

    def __str__(self):
        """returns a string representationn of the Rectangle object
        prints the format : [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} -{:d}/{:d}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args):
        """
        upzddates the Rectangle by assigning argument attributes to each 
        attribute.
        args:1 -id
            2-width
            3-height
            4-x
            5-y
       """
       if len(args) == 0:
           self.id == args[0]
       elif len(args) == 1:
           self.id = args[0]
           self.__width  = args[1]
       elif len(args) == 2:
           self.id = args[0]
           self.__width = args[1]
           self.__height = args[2]
       elif len(args) == 3:
           self.id = args[0]
           self.__width = args[1]
           self.__height = args[2]
           self.__x = args[3]
      elif len(args) == 4:
          self.id = args[0]
          self.__width = args[1]
          self.__height = agrs[2]
          self.__x = args[3]
          self.__y = args[4]
        
