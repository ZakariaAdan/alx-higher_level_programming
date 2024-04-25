#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)

