#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
basic struct graph, containing vertices and edges
"""

from log import logger
l = logger.getLogger("keepindoors/spark/spark.py")

from mongodb.mongo_cli import *

class graph(object):
    """
    graph struct
    """
    # nodes set V, containing all nodeId [nodeId1,nodeId2...]
    vertices = set()
    # edges set E, containing all edgeID [(v1,v2),(v3,v4)]. v is the nodeId ,and v1 < v2
    edges = set()
    # graphId, using uuid, for example 'da0d7ceb-4b97-11e8-aaec-8c8590861163'
    id = ''
    # graph info
    info = {}

    def loadEdgesFromMongo(self,mongo_cli,databbase_name,collection_name):
        """
        load doc_pairs as Edges from mongo db
        :param mongo_cli:
        :param databbase_name:
        :param collection_name:
        :return:
            the set of Edges
        """
        c = getCollection(mongo_cli, databbase_name, collection_name)
        for r in c.find():
            self.edges.add((r["docno1"],r["docno2"]))
        return self.edges