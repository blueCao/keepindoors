"""
the running script of the project in python env

cron job:
    1. load new docs from mongodb
    2. extract the topK <word,weight> from every doc
    3. caculate the [distance] between the new docs , old docs  and the new docs itself
    4. insert the [distande] values into mongodb
    5. system call : sparksubmit using graphx and wait for finishing (in spark, insert [component] into mongodb)
    6. update the web view
"""
from log.logger import *
log = getLogger("keepindoors.run")

# ************************************** 1. load new docs(3 hours ago) from mongodb

from bson.objectid import ObjectId
from datetime import datetime, timedelta
import mongodb.mongo_cli as mongo

# create datetime, 8 hours is time zone loss
three_hours_ago = datetime.now() - timedelta(hours=8,minutes=15)
dummy_id = ObjectId.from_datetime(three_hours_ago)

#  mongodb
dbname = "keepindoors"
collname = "docs"
cli = mongo.__get__()
collection = mongo.getCollection(cli,dbname,collname)
cursor = collection.find({"_id":{"$gt":dummy_id}})
new_docs = []
for d in cursor:
    new_docs.append(d)

# ************************************** 2. extract the topK <word,weight> from every doc
from core.textrank import *
textrank(new_docs)

# ************************************** 3. caculate the [distance] between the new docs , old docs  and the new docs itself
from core.simhash import *

# load old doc
cursor = collection.find({"_id":{"$lte":dummy_id}})
old_docs = []
for d in cursor:
    old_docs.append(d)

# distance between new_docs itself
MIN_DISTANCE = 6
distances = []
new_docs_size = len(new_docs)
for index_a in range(new_docs_size):
    for index_b in range(index_a+1,new_docs_size):
        simhash_a = new_docs[index_a]["simhash"]
        simhash_b = new_docs[index_b]["simhash"]
        d = distance(simhash_a,simhash_b)
        if d <= MIN_DISTANCE:
            distances.append({"docno1":new_docs[index_a]["docno"],"docno2":new_docs[index_b]["docno"],"distance":d})
            log.info("<3> distance between new_docs itself :"+ str({"docno1":new_docs[index_a]["docno"],"docno2":new_docs[index_b]["docno"],"distance":d}))

# distance between new_docs and old_docs
old_docs_size = len(old_docs)
for d_a in new_docs:
    for d_b in old_docs:
        d = distance(d_a["simhash"],d_b["simhash"])
        if d <= MIN_DISTANCE:
            distances.append({"docno1": d_a["docno"], "docno2": d_b["docno"], "distance": d})
            log.info("<3> distance between new_docs and old_docs :"+str({"docno1": d_a["docno"], "docno2": d_b["docno"], "distance": d}))


# ************************************** 4. insert the [distande] values into mongodb
collname = "distances"
if distances:
    # filter the duplicated
    for d in distances:
        if mongo.getCollection(cli,dbname,collname).find_one({"docno1":d["docno1"],"docno2":d["docno2"]}) or mongo.getCollection(cli, dbname, collname).find_one({"docno1": d["docno2"], "docno2": d["docno1"]}):
            continue
        mongo.insertDoc(d, cli, dbname, collname)
        log.info("<4> insert the distance: "+str(d)+"  into mongodb")
    # ************************************** 5. system call : sparksubmit using graphx and wait for finishing (in spark, insert [component] into mongodb)
    import os

    # run sparksubmit
    spark_path = "~/spark-2.3.0-bin-hadoop2.7/bin/spark-submit"
    python_zip_path = "/home/hadoop/workspace/python/keepindoors/keepindoors.zip"
    python_job_path = "/home/hadoop/workspace/python/keepindoors/spark-submit-jobs/connectedComponentsJob.py"
    spark_cmd = spark_path + \
          " --master yarn --deploy-mode client --packages graphframes:graphframes:0.5.0-spark2.1-s_2.11" \
          " --executor-memory 4g --queue default"+\
          " --py-files  " + python_zip_path + \
          " " + python_job_path
    os.system(spark_cmd)
    log.info(spark_cmd)
    log.info("<5> spark graphx command finished!")
else:
    log.info("<4> new distances is empty,finished!")