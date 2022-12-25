#!/usr/bin/python3
"""Square that defines a square """


class Square:
    """ a class that returns the area of a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return pow(self.__size, 2)

    @property
    def position(self):
        return self.__size

    @size.setter
    def position(self, value):
        if isinstance(value,int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
    def my_print(self):
        for i in range(self.__size ** 2):
            if (i % self.__size == 0) and i != 0:
                print()
            print("#",end="")
        print()
             

