#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    m = my_list[0]
    for d in my_list:
        if d > m:
            m = d
    return m
