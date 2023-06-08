#!/usr/bin/python3
import sys


if __name__ == "__main__":
    lenght = len(sys.argv)
    print(f"{lenght - 1} argument", end="")
    if lenght == 1:
        print(".")
    elif lenght == 2:
        print(":")
        print(f"1: {sys.argv[1]}")
    else:
        print("s:")
        for i in range(1, lenght):
            print(f"{i}: {sys.argv[i]}")
