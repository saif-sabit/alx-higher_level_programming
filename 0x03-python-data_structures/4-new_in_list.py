#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list)- 1:
        return my_list
    else:
        my_new_list = my_list.copy()
        my_list[idx] = element
        return my_new_list