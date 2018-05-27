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
        r["id"] = i
        r["name"] = str(i)
        localVertices.append(r)
        i = i + 1

    # e
    localEdges = []
    cursor = mongo.getCollection(cli, "keepindoors", "doc_pairs").find()
    # for r in cursor:
    #     # del "_id" key which will throws error when createDataFrame
    #     if "_id" in r.keys():
    #         del r["_id"]
    #     localEdges.append(r["same"])
    localEdges = cursor.next()["same"]

    v = spark.createDataFrame(localVertices)
    e = spark.createDataFrame(localEdges, ["distance","src", "dst"])
    g = GraphFrame(v,e)
    # get sparkContext from sparkSession
    spark.sparkContext.setCheckpointDir("/tmp/spark/checkpoint")
    result = g.connectedComponents()

    # save in hdfs
    result.write.format("csv").save("/tmp/spark/graphframes.csv")

if __name__ == "__main__":
    main()