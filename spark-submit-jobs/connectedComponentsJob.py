#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
spark job,using graphx caculate the connected Components
"""

import mongodb.mongo_cli as mongo
from pyspark.sql import SparkSession
from graphframes import GraphFrame

def main():
    # crate spark session
    spark = SparkSession.builder.appName("keepindoors graphx connectedComponents()").getOrCreate()

    # get a mongo client
    cli = mongo.__get__()

    # v
    localVertices=[]
    cursor = mongo.getCollection(cli,"keepindoors","docs").find()
    i = 0
    for r in cursor:
        # del "_id" key which will throws error when createDataFrame
        if "_id" in r.keys():
            del r["_id"]
        if "simhash" in r.keys():
            del r["simhash"]
        r["id"] = r["docno"]
        r["name"] = str(i)
        localVertices.append(r)
        i = i + 1

    # e
    localEdges = []
    cursor = mongo.getCollection(cli, "keepindoors", "distances").find()
    # for r in cursor:
    #     # del "_id" key which will throws error when createDataFrame
    #     if "_id" in r.keys():
    #         del r["_id"]
    #     localEdges.append(r["same"])
    localEdges = []
    for r in cursor:
        localEdges.append((r["docno1"],r["docno2"],r["distance"]))

    v = spark.createDataFrame(localVertices)
    e = spark.createDataFrame(localEdges, ["src", "dst","distance"])
    g = GraphFrame(v,e)
    # get sparkContext from sparkSession
    spark.sparkContext.setCheckpointDir("/tmp/spark/checkpoint")
    result = g.connectedComponents()

    # save in hdfs
    result.write.format("json").save("/tmp/spark/graphframes.json")

if __name__ == "__main__":
    main()