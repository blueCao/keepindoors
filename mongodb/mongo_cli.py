#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
unique global  mongo cli

database:
        keepindoors
collection:
        docs
                field:
                        _id     12字节的随机数(mongodb自动产生)    https://docs.mongodb.com/manual/reference/method/ObjectId/#description
                        docno
                        url
                        content
                        title
                        date

        doc_pairs
                field:
                        _id
                        docno1
                        docno2

"""

import pymongo

def __get__():
    return pymongo.MongoClient("localhost", 27017)

def insertDoc(doc,mongo_cli,databbase_name,collection_name):
    """
        insert one document into mongodb
    :param mongo_cli:
    :param doc:
        document that will be insert into mongodb
    :param databbase_name:
    :param document_name:
    :return:
        pymongo.results.InsertOneResult with a inserted id
    """
    c = getCollection(mongo_cli,databbase_name,collection_name)
    return c.insert_one(doc)

def insertDocs(docs,mongo_cli,databbase_name,collection_name):
    """
        insert many documents into mongodb
    :param mongo_cli:
    :param docs:
        A iterable of documents to insert.
    :param databbase_name:
    :param collection_name:
    :return:
        pymongo.results.InsertManyResult with many inserted id
    """
    c = getCollection(mongo_cli, databbase_name, collection_name)
    return c.insert_many(docs)

def getCollection(mongo_cli,databbase_name,collection_name):
    """
        get specified collection
    :param mongo_cli:
    :param databbase_name:
    :param collection_name:
    :return:
        pymongo.collection.Collection
    """
    return mongo_cli.get_database(databbase_name).get_collection(collection_name)

def deleteOne(filter,mongo_cli,databbase_name,collection_name):
    """
    delete one document according to the filter
    :param mongo_cli:
    :param databbase_name:
    :param collection_name:
    :param filter:
    :return:
        pymongo.results.DeleteResult
    """
    c = getCollection(mongo_cli, databbase_name, collection_name)
    return c.delete_one(filter)

def deleteMany(filter,mongo_cli,databbase_name,collection_name):
    """
    delete many documents according to the filter
    :param mongo_cli:
    :param databbase_name:
    :param collection_name:
    :param filter:
    :return:
        pymongo.results.DeleteResult
    """
    c = getCollection(mongo_cli, databbase_name, collection_name)
    return c.delete_many(filter)

def deleteAll(mongo_cli,databbase_name,collection_name):
    """
    delete all documents
    :param mongo_cli:
    :param databbase_name:
    :param collection_name:
    :return:
        pymongo.results.DeleteResult
    """
    return deleteMany({},mongo_cli,databbase_name,collection_name)

class MongoCli(object):
    cli = None