#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python str、byte、utf8 transform
"""

def str2utf8(s):
    """
    type string convert to utf8 unicode string
    :param s: the input string
    :return: the output unicode utf_8 string
    """
    assert isinstance(s,str)
    return s.encode("unicode_escape").decode("utf-8")

def pattern2utf8(p):
    """
    pattern string for regex match
    :param p: the original pattern string
    :return: the replaced match
    """
    assert isinstance(p,str)
    return str2utf8(p).replace("\\","\\\\")

def utf2str(u):
    """
    utf8 string convert to str
    :param u: utf8 based str
    :return: converted str
    """
    assert isinstance(u,str)
    return u.encode("utf_8").decode("unicode_escape")