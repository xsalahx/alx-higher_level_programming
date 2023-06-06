#!/usr/bin/python3
toggle = True
for i in range(122, 96, -1):
    if toggle == True:
        print(f"{chr(i)}", end="")
        toggle = False
    else:
        shift = ord('a') - ord('A')
        print(f"{chr(i - shift)}", end="")
        toggle = True
