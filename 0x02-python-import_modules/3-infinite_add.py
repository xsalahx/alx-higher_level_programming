#!/usr/bin/python3
import sys
if __name__ == "__main__":
    s = 0
    for d in sys.argv[1:]:
        s = s + int(d)
    print(s)
