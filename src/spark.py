#!/usr/bin/python3

from pyspark import SparkConf, SparkContext

# Initialize a Session
conf = SparkConf().setAppName("wordcountapp")
conf.set("spark.hadoop.fs.defaultFS", "hdfs://namenode:8020")

spark = SparkContext(conf=conf)

# Read a text file
lines = spark.textFile("hdfs://namenode:8020/input.txt")

# Step 3: Split each line into words and create RDDs
rdds = lines.flatMap(lambda line: line.split(" "))

# Step 4: Map each word to a pair of (word, 1)
# Contrary to MapReduce, Spark does not require the output of the map
# function to be a key-value pair and stores it in memory as an RDD
# instead of writing it to disk. (unless the memory is full)
word_pairs = rdds.map(lambda word: (word, 1))

# Step 5: Reduce by key (word) to count the occurrences of each word
# The reduceByKey transformation is a transformation that shuffles the data
# across partitions to perform the reduce operation. It also runs the reduce
# operation in memory and in parallel (if the memory allows it).
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)  # type: ignore

# Step 6: Save the results to a text file/s (in HDFS)
# Spark generates multiple output files proportional to the number of
# partitions in the RDD. The output files are stored in a directory
# specified by the path (unless specified after partitioning RDD/s)
word_counts.saveAsTextFile("hdfs://namenode:8020/output")

# Step 7: Stop the Session
spark.stop()
