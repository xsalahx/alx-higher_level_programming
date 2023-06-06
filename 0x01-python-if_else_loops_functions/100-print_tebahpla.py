#!/usr/bin/python3
toggle = True
for i in range(122, 96, -1):
    if toggle is True:
        print("{}".format(chr(i)), end="")
        toggle = False
    else:
        shift = ord('a') - ord('A')
        print("{}".format(chr(i - shift)), end="")
        toggle = True
