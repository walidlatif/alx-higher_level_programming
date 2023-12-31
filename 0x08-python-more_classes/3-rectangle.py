#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a Rectangle object"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that return the width

        Returns:
            Rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that return the height

        Returns:
            Rectangle height

        """

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the rectangle area

        Returns:
            return the rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """Method that returns the rectangle perimeter

        Returns:
            if width or height is equal to 0, perimeter is equal to 0
            return the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Method that returns a string that represents the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
