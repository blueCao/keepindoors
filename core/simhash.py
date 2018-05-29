#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
similarity hash algorithm to caculate the text similarity
"""

# get system max int length
import sys
INT_BITS_LENGTH=len(bin(sys.maxsize)) - 1

def simhash(textrank, threshold=0):
    """
    caculate the hash value of the textrank topK value
    :param textrank: list(duple) type, contains a word and a weight
    :param threshold: the thredshold value which determines the result each bit 0 or 1
    :return: the hash value(int)
    """
    # each position is a sum of all words' hash value
    sum = []
    for i in range(INT_BITS_LENGTH):
        sum.append(0)
    for word,weight in textrank:
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
    for i in range(INT_BITS_LENGTH):
        if sum[i] > threshold:
            result = result + (1 << i)
    return result

def distance(simhash_1,simhash_2):
    """
    the mindistance of two value
    :param simhash_1: hash value 1
    :param simhash_2: hash value 2
    :return: the minimal edit distance of them
    """
    v = simhash_1 ^ simhash_2
    bin_str = bin(v)[2:INT_BITS_LENGTH]
    dist = 0
    # caculate the 1 numbers
    for b in bin_str:
        if int(b) > 0:
            dist = dist + 1
    return dist