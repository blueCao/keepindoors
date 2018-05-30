from pyspark.sql import SparkSession
from graphframes import GraphFrame
import mongodb.mongo_cli as mongo
from datetime import timedelta

def main():
    # crate spark session
    spark = SparkSession.builder.appName("keepindoors graphx connectedComponents()").getOrCreate()

    # get a mongo client
    cli = mongo.__get__()

    # v, ["id","url","title","datetime"]
    localVertices=[]
    cursor = mongo.getCollection(cli,"keepindoors","docs").find()
    for r in cursor:
        # del "_id" key which will throws error when createDataFrame
        r["id"] = r["docno"]
        localVertices.append((r["docno"],r["url"],r["title"],str(r["_id"].generation_time + timedelta(hours=8))))

    # e
    cursor = mongo.getCollection(cli, "keepindoors", "distances").find()
    localEdges = []
    for r in cursor:
        localEdges.append((r["docno1"],r["docno2"],r["distance"]))

    v = spark.createDataFrame(localVertices,["id","url","title","datetime"])
    e = spark.createDataFrame(localEdges, ["src", "dst","distance"])
    g = GraphFrame(v,e)
    # get sparkContext from sparkSession
    spark.sparkContext.setCheckpointDir("/tmp/spark/checkpoint")
    result = g.connectedComponents()

    # order by component,datetime
    result = result.orderBy(["component", "datetime"], ascending=[1, 0]).collect()

    # create component dict
    component_dict = {}
    for row in result:
        record = row.asDict()
        if record["component"] not in component_dict.keys():
            component_dict[record["component"]] = []
        component_dict[record["component"]].append(record)

    # delete mongo collection "component"
    mongo.deleteAll(cli,"keepindoors","components")

    # save component_dict into mongo
    index = 1
    for key,item in component_dict.items():
        links = []
        titles = []
        title = "empty title"
        update_time = "1970-01-01 00:00:00+00:00"
        for doc in item:
            titles.append(doc["title"])
            links.append(doc["url"])
            if doc["datetime"] > update_time:
                update_time = doc["datetime"]
                title = doc["title"]
        mongo.insertDoc({"no":index,"component":key,"title":title,"size":len(item),"links":links,"titles":titles,"docs":item},cli,"keepindoors","components")
        index += 1

    # save in hdfs
    # result.write.format("json").save("/tmp/spark/graphframes.json")

if __name__ == "__main__":
    main()