#!/usr/bin/python3
""" The Square Module.

This module contains a class that defines a square
and __init__ method that sets its size with
and Integer only
and another method that 'area' that calculates
area and setter and getter method the get or sets it
then prints a square with size 'size' """


class Square:

    """Defines a square."""
    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints a square in size 'size' with '#'"""
        num = self.__size
        if num == 0:
            print()
        for i in range(num):
            print('#' * num)
