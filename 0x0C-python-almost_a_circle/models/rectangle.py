#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    Initialize a Rectangle instance
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x position of rectangle
        y (int): y position of rectangle
        id (int): id of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter
        Returns:
            rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Args:
            value (int): rectangle width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter
        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        Args:
            value (int): rectangle height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter
        Returns:
            rectangle position : x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter
        Args:
            value (int): rectangle position : x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter
        Returns:
            rectangle position : y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter
        Args:
            value (int): rectangle position : y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calcul the Rectangle instance.
        Returns:
            returns the area value of the Rectangle instance.
        """
        return self.height * self.__width

    def display(self):
        """
        Function that prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each attribute
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        attribute_names = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attribute_names[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representing the rectangle.

        Returns:
            dict: A dictionary containing the rectangle's
            attributes (id, width, height, x, y).
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
