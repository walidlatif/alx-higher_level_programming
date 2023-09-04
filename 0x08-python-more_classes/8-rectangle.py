#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a Rectangle object

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (string)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return "\n".join([str(self.print_symbol) *
                          self.__width] * self.__height)

    def __repr__(self):
        """Method that returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Method Print the message Bye rectangle...
        (... being 3 dots not ellipsis) when
        an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to determine the larger
           rectangle based on their areas.

        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
            The larger of the two rectangles.
            If they have the same area, rect_1 is returned.

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
