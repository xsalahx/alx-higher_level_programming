#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = []
    for d in my_list:
        if d % 2 == 0:
            lst.append(True)
        else:
            lst.append(False)
    return lst
