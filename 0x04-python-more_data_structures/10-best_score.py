#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            if value >= x:
                ret = key
        return ret
    else:
        return None
