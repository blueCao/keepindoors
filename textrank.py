#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
text rank from module jieba
"""
import jieba
import jieba.analyse
from xml_handler import generate_xml_from_doc_list

def textrank(list,xml_file_name='textrank.xml'):
    """
    caculate the textrank algorithm and get the topK text rank  info and write into the xml file
    :param list: input doc list
    :return:
    """
    for d in list:
        d.textrank = jieba.analyse.textrank(d.content, 10,True)
    generate_xml_from_doc_list(list,xml_file_name)