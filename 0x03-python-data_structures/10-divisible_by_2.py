#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = []
    for d in my_list:
        lst.append(d % 2 == 0)
