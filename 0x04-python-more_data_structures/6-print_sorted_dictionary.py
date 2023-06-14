#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k_list = list(a_dictionary.keys())
    k_list.sort()
    for i in k_list:
        print("{}:{}".format(i, a_dictionary.get(i)))
