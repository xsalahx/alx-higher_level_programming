#!/usr/bin/python3
def uppercase(str):
    if ord(c) >= ord('a') and ord(c) <= ord(z):
        shift = - ord('a') + ord('A')
    for c in str:
        print("{}".format(chr(ord(c) - ord('a') + ord('A'))), end="")
    print("\n")
