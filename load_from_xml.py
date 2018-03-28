import xml_handler as h

# load data into memory
handler = h.load_data_from_xml("output_samples_20120615_to_20120615.xml")
# remove the duplicated data
unique_list = h.unique(handler.doc_list)
