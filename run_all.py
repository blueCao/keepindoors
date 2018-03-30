import xml_handler as h
import simhash
import datetime

"""
the running script of the project
"""

def show_time(msg):
    """
    print current time and a message,return current time_stamp
    :param msg:
    :return: current time_stamp
    """
    current = datetime.datetime.now()
    print(current)
    print(msg)
    print()
    return current

# show begin time
begin_time_stamp=show_time("begin")

# load data into memory
handler = h.load_data_from_xml("textrank.xml")

# show minmash begin time
begin_minhash_time_stamp=show_time("begin minhash caculate")

# caculate simhash of each doc
doc_size = len(handler.doc_list)
threshold = 0
simhashes = []
for index_a in range(doc_size):
    simhashes.append(simhash.simhash(handler.doc_list[index_a].textrank, threshold))

# show minmash distances caculate begin time
begin_distances_time_stamp=show_time("begin minhash distances caculate")

#  caculate each pair distance of doc
#  distances is a 2D array
distances = []
for index_a in range(doc_size):
    distances.append([])
    for index_b in range(index_a+1,doc_size):
        simhash_a = simhashes[index_a]
        simhash_b = simhashes[index_b]
        distances[index_a].append(simhash.distance(simhash_a,simhash_b))

# show minmash distances caculate begin time
end_time_stamp=show_time("all finished!")

# display the similar doc
min_distance = 6
same = []
for index_a in range(doc_size):
    for index_b in range(index_a+1,doc_size):
        d = distances[index_a][index_b - index_a - 1]
        if d <= min_distance:
            same.append((d,index_a,index_b))
            print(distances[index_a][index_b-index_a-1])
            print(index_a)
            print(index_b)
            print(" ")