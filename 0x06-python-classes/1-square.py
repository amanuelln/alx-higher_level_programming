#!/usr/bin/python3
""" The Square Module.

This module contains a class that defines a square and __init__ method that sets its size
"""
class Square:
    '''
    Defines a square.
    '''

    def __init__(self, size):
        """Sets necessary attributes for the square object

        Args:
            size (int): size of edge of square"""
        self.__size = size
