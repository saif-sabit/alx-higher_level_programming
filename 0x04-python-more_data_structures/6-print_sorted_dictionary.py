#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k_list = list(a_dictionary.keys())
    k_list.sort()
    sorted_dict = {i: a_dictionary[i] for i in k_list}
    for k, v in sorted_dict.items():
        print("{}:{}".format(k, v))
