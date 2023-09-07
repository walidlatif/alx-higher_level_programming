#!/usr/bin/python3
'''Module that prints a square with the character #.'''


def print_square(size):
    ''' Print a square with char #

    Args:
        size (int):  is the size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 1
    while i <= size:
        print("#" * size)
        i += 1
