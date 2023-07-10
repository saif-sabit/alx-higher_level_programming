#!/usr/bin/python3
"""Class child of list class"""
class MyList(list):
    """ Implements print for list class"""
    def print_sorted(self):
        """ prints list"""
        print(sorted(self))