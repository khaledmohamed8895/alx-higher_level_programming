#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        char = sentence[0]
        return (a, char)
    else:
        return (0, None)
