#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        char = None
    else:
        char = sentence[0]
    return lenght, char
