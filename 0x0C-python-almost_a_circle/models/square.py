#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """
        Call the super class with id, x, y, width and height
        width and height assigned to size
        """
    def __str__(self):
        """
        method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter
        Returns:
            Square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value (int): rectangle size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each attribute
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        attribute_names = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attribute_names[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representing the square.

        Returns:
            dict: A dictionary containing the square
            attributes (id, x, size, y).
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
