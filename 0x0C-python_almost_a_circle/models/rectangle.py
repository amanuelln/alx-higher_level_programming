#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Width getter and setter

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")      
        else:
            raise TypeError("width must be an integer")

    # height getter and setter 
    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
    # x getter and setter 

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")


    def area(self):
        """Returns the area"""
        return self.__height * self.__width
    
    def display(self):
        """String representation of this rectangle"""
        for z in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Returns string info"""
        string_for_format = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        string_for_format = string_for_format.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return string_for_format


    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None:
            for idx, value in enumerate(args):
                setattr(self, attributes[idx], value)
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representaion of this class"""
        return {'x': self.x, 'y':self.y, 'id': self.id, 'height': self.height,  'width': self.width}
