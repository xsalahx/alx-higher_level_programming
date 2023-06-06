#!/usr/bin/python3
def uppercase(str):
    for c in str:
        shift = 0
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            shift = - ord('a') + ord('A')
        print("{}".format(chr(ord(c) + shift)), end="")
    print("\n")
