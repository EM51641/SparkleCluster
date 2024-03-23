FROM apache/hadoop:3

RUN sudo yum install python3 -y

COPY input.txt /opt/hadoop/input.txt

COPY src/mapper.py /opt/hadoop/mapper.py

COPY src/reducer.py /opt/hadoop/reducer.py

COPY src/spark.py /opt/hadoop/spark.py

COPY run_map_reduce.sh .

COPY run_spark.sh .

RUN sudo chmod +x run_map_reduce.sh &&\
    sudo chmod +x run_spark.sh
