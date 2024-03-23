hdfs dfs -put input.txt hdfs://namenode/

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files "mapper.py,reducer.py" -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input hdfs://namenode/input.txt -output output.txt
