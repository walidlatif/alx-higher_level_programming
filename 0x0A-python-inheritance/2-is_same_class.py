#!/usr/bin/python3
'''
Module : is_same_class that check the object is
exactly an instance of the specified class
'''


def is_same_class(obj, a_class):
    """
    Determines whether an object is an exact instance of the provided class.

    Args:
        obj (any): The object to be evaluated.
        a_class (any): The class to compare against.

    Returns:
        bool: True if the object is precisely an
        instance of the specified class.
    """

    return type(obj) == a_class
