#!/usr/bin/python3

def multiple_returns(sentence):
    len_ = len(sentence)
    if len_ == 0:
        result = (0, None)
        return result
    else:
        res = (len_, sentence[0:1])
        return res
