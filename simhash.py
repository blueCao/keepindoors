#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
similarity hash algorithm to caculate the text similarity
"""

def hash(textrank, threshold):
    """
    caculate the hash value of the textrank topK value
    :param textrank: dict type, contains a word and a weight
    :param threshold: the thredshold value which determines the result each bit 0 or 1
    :return: the hash value(int)
    """
    # each position is a sum of all words' hash value
    sum = []
    for word,weight in textrank:
        # 1. hash value of single word
        h = hash(word)
        # 2. spilte hash value into 1 or 0
        b_str = bin(h)
        b_str = bin(h)[2:len(b_str)]
        # 3. binary string convert to 1 or 0 and sum up all the value plus weight
        b_int = []
        for b in b_str:
            b_int = int(b)
        # 4.