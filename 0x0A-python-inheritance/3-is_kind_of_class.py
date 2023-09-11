#!/usr/bin/python3
"""
Module : is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (any): The class to compare against.

    Returns:
        bool: True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified
        class; otherwise, False.
    """
    return isinstance(obj, a_class)
