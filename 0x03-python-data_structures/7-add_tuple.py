#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = [0, 0]
    for i in range(min(2, len(tuple_a))):
        lst[i] += tuple_a[i]
    for i in range(min(2, len(tuple_b))):
        lst[i] += tuple_b[i]
    return (lst[0], lst[1])
