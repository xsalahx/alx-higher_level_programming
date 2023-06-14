#!/usr/bin/python3
def best_score(a_dictionary):
    h_key = None
    m = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] >= m:
            m = a_dictionary[key]
            h_key = key
    return h_key
