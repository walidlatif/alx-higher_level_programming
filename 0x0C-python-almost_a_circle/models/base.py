#!/usr/bin/python3
''' Base class '''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a dictionary representing the Base.

        Returns:
            dict: A dictionary containing the Base's
            attributes (x, width, id, height, y).
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
