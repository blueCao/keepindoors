#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the running script
"""
import xml_handler as h

# load data into memory
handler = h.load_data_from_xml("input.xml")

# sort the doc_list
my_alphabet = ['0', '1', '2','3', '4', '5','6','7', '8', '9'];
def custom_key(doc):
   numbers = []
   for letter in doc.date:
      numbers.append(my_alphabet.index(letter))
   return numbers
handler.doc_list.sort(key=custom_key)

# wirte output xml file
h.generate_xml_from_doc_list(handler.doc_list,"output.xml")