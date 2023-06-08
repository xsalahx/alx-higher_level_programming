#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    print(f"{l - 1} argument", end="")
    if l == 1:
        print(".")
    elif l == 2:
        print(":")
        print(f"1: {sys.argv[1]}")
    else:
        print("s:")
        for i in range(1, l):
            print(f"{i}: {sys.argv[i]}")

