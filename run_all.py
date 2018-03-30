import xml_handler as h
import simhash

# load data into memory
handler = h.load_data_from_xml("textrank.xml")

#  caculate each pair distance of doc
#  distances is a 2D array
threshold = 0
distances = []
doc_size = len(handler.doc_list)
for index_a in range(doc_size):
    distances.append([])
    for index_b in range(index_a+1,doc_size):
        simhash_a = simhash.simhash(handler.doc_list[index_a].textrank, threshold)
        simhash_b = simhash.simhash(handler.doc_list[index_b].textrank, threshold)
        distances[index_a].append(simhash.distance(simhash_a,simhash_b))

# display the similar doc
min_distance = 6
same = []
for index_a in range(doc_size):
    distances.append([])
    for index_b in range(index_a+1,doc_size):
        d = distances[index_a][index_b - index_a - 1]
        if d <= min_distance:
            same.append((d,index_a,index_b))
            print(distances[index_a][index_b-index_a-1])
            print(index_a)
            print(index_b)
            print(" ")