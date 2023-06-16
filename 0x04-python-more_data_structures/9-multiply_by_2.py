#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = {}
    if (a_dictionary):
        for key, value in a_dictionary.items():
            ret[key] = value * 2
    return ret
