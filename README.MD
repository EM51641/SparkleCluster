# SparkleCluster

SparkleCluster is a template that leverages HDFS and YARN to run containerized Spark or MapReduce jobs. It provides a robust and scalable solution for processing large datasets.

## Features

- Distributed processing using Hadoop's YARN and HDFS.
- Containerized environment for easy setup and deployment.
- Spark or MapReduce for efficient data processing.
- Job History Server (HS) for monitoring and debugging.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the SparkleCluster repository to your local machine.

2. Navigate to the project directory.

3. Build and start the Docker containers:

   ```bash
   docker-compose up -d
   ```

### Running a MapReduce Job

1. Access the `namenode` Docker container:

   ```bash
   docker exec -it namenode bash
   ```

2. Navigate to the `/opt/hadoop` directory:

   ```bash
   cd /opt/hadoop
   ```

3. Run the `run_map_reduce.sh` script to start a MapReduce job:

   ```bash
   ./run_map_reduce.sh
   ```

## Monitoring

You can monitor the progress of your MapReduce jobs and view completed jobs using the Hadoop Job History Server. By default, the Job History Server's web interface is accessible at `http://<hostname>:19888`, where `<hostname>` is the name or IP address of the machine running the Job History Server.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
