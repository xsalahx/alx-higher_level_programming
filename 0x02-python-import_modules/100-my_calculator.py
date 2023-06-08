#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            op = add
        elif sys.argv[2] == '-':
            op = sub
        elif sys.argv[2] == '*':
            op = mul
        else:
            op = div
        print(f"{a} {sys.argv[2]} {b} = {op(a, b)}")
