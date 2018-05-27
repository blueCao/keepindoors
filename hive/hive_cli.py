#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hive cli
"""

from log import logger
l = logger.getLogger("keepindoors/hive/hive_cli.py")

def loadRowsFromHive(self,spark,table_name):
    """
    load row list from hive ,specifying the table_name

    :param spark:
        pyspark.sql.session.SparkSession
    :param table_name:
        string
    :return:
        list of pyspark.sql.Row
        if table is not exist, return None
    """
    try:
        return spark.sql("select * from "+table_name).limit()
    except:
        l.error("Table':"+table_name+"' is not exist!")
        return None