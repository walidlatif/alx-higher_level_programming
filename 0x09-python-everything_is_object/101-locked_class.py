#!/usr/bin/python3
"""Module LockedClass"""


class LockedClass:
    """
    This class restricts the dynamic creation of new instance attributes,
    except when the attribute is named 'first_name'.

    Attributes:
        first_name (str): The first name of something.
    """

    __slots__ = ['first_name']
