#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        return None
    else:
        b = sentence[0]
        return a, b
