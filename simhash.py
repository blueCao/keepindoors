#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
similarity hash algorithm to caculate the text similarity
"""

def simhash(textrank, threshold=0):
    """
    caculate the hash value of the textrank topK value
    :param textrank: dict type, contains a word and a weight
    :param threshold: the thredshold value which determines the result each bit 0 or 1
    :return: the hash value(int)
    """
    # each position is a sum of all words' hash value
    sum = []
    for i in range(32):
        sum.append(0)
    for word,weight in textrank.items():
        # 1. hash value of single word
        h = abs(hash(word))
        # 2. spilte hash value into 1 or 0
        b_str = bin(h)
        b_str = bin(h)[2:len(b_str)]
        # 3. binary string convert to 1 or 0 and sum up all the value plus weight
        start_index = len(b_str) - 1
        for b in b_str:
            b_int = int(b)
            if b_int > 0:
                sum[start_index] = sum[start_index] +  weight
            else:
                sum[start_index] = sum[start_index] - weight
            start_index = start_index - 1
    # convert the sum into binary
    result = 0
    for i in range(32):
        if sum[i] > threshold:
            result = result + (1 << i)
    return result