#!/usr/bin/python3
""" The Square Module.

This module contains a class that defines a
square and __init__ method that sets its size with
and Integer only
and another method that 'area' that calculates area"""


class Square:
    """Defines square with private instance attribute size and a method area

    """

    def __init__(self, size):
        """
        contains the neccessary attributes

        Args:
            size (int): size of the edge of square

        raises:
            TypeError: If size is not integer
            ValueError: If size value is not intefer"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
