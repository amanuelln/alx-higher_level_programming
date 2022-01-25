#!/usr/bin/python3
""" The Square Module.

This module contains a class that defines a
square and __init__ method that sets its size with
and Integer only
"""


class Square:
    """
     Defines a square that has private instance attribute called 'size'
     """

    def __init__(self, size=0):
        """
        contains a necessary attributes for square

        Args:
            size (int): size of the edge of the square

        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
