# Script to manage streaming of data

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: kafka-spark-car.py <zk> <topic>", file=sys.stderr)
        exit(-1)
    
    sparkConf = SparkConf()
    sparkConf.setMaster("local[*]").setAppName("PythonStreamingKafkaSpark")
    
    spark = SparkSession.builder.config(conf=sparkConf).getOrCreate()
    
    # Construct a streaming DataFrame that reads from testtopic
    df = spark.readStream  \
         .format("kafka")  \
         .option("kafka.bootstrap.servers", sys.argv[1])  \
         .option("subscribe", sys.argv[2])  \
         .option("startingOffsets", "earliest")  \
         .load()
    
    # Define a schema for the data received
    schema = StructType([     
        StructField("id_sensor", StringType(), True),
        StructField("destination", StringType(), True),
        StructField("road_type", StringType(), True),
        StructField("speed_limit", IntegerType(), True),
        StructField("model", StringType(), True),
        StructField("plate", StringType(), True),
        StructField("eventTime", StringType(), True),
        StructField("speed", IntegerType(), True)
    ])
    
    # Take data in json format
    dataset = df.withColumn("value", from_json(col("value").cast("string"), schema))
    data = dataset.select(col("value.*"))
    
    data = data.withColumn("speed_limit", data["speed_limit"].cast(IntegerType()))
    data = data.withColumn("speed", data["speed"].cast(IntegerType()))
    
    # Visualize the set of cars that have a speed beyond the speed limits
    table = data.filter((data["speed"] - data["speed_limit"]) > 0)
    table = table.withColumn("speeding(km/h)", table["speed"] - table["speed_limit"])
    table = table.select("plate", "model", "speeding(km/h)")
    
    query1 = table.writeStream  \
            .outputMode("update")  \
            .format("console")  \
            .option("truncate", False)  \
            .option("numRows", 10000)  \
            .trigger(processingTime="5 seconds")  \
            .start()  \
            .awaitTermination()

