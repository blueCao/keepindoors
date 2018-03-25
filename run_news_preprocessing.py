#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the running script
"""
import xml.sax
import xml as h

# create a XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# Overwrite ContextHandler
handler = h.xml_news_handler()
parser.setContentHandler(handler)

# parse xml file
parser.parse("news_tensite_xml.smarty.xml")

# sort the doc_list
my_alphabet = ['0', '1', '2','3', '4', '5','6','7', '8', '9'];
def custom_key(doc):
   numbers = []
   for letter in doc.date:
      numbers.append(my_alphabet.index(letter))
   return numbers
handler.doc_list.sort(key=custom_key)