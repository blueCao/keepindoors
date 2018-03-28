#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the running script to only sampling part of data between begin date and end date
"""
import xml.sax
import xml_handler as h

# create a XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# Overwrite ContextHandler
handler = h.xml_news_handler()
parser.setContentHandler(handler)

# parse xml file
parser.parse("input.xml")

# sort the doc_list
my_alphabet = ['0', '1', '2','3', '4', '5','6','7', '8', '9'];
def custom_key(doc):
   numbers = []
   for letter in doc.date:
      numbers.append(my_alphabet.index(letter))
   return numbers
handler.doc_list.sort(key=custom_key)

# sampling from the list of doc
begin_date ="20120601"
end_date = "20120601"
samples=h.sample(handler.doc_list,begin_date,end_date)
# wirte output xml file
h.generate_xml_from_doc_list(samples,"output_samples_"+begin_date+"_to_"+end_date+".xml")