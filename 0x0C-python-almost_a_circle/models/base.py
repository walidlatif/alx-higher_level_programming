#!/usr/bin/python3
''' Base class '''


class Base:
    """Represent a Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base.

        Args:
            id : Base id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
