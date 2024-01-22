#!/usr/bin/python3
def multiple_returns(sentence):
    '''a function that returns a tuple.'''
    if len(sentence) == 0:
        first = None
        length = len(sentence)
        return length, first

    else:
        first = list(sentence)
        length = len(sentence)
        return length, first[0]
