#!/usr/bin/python3
"""  Function  prints a square with the # char """


def print_square(size):
    """ We print a size x size square out and are happy with it

    Args:
        Size: the size of the square we ant printed

    Return: no return
    """
    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
