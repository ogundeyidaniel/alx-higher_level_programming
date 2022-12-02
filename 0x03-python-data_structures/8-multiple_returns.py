#!/usr/bin/python3


def multiple_returns(sentence):
    first = sentence[0] if sentence != '' else None
    tup = (len(sentence), first)
    return tup
