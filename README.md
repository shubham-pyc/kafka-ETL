# Kafka Application

This project demonstrates a producer-consumer model using Apache Kafka to generate 10 million events. The events are produced by a Kafka producer and consumed by a consumer, which writes them to MongoDB.



# Installations

Download kafka
```shell
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
tar -xzf kafka_2.12-2.8.0.tgz
```

Open new terminal and Run zookeeper
```shell
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Open new terminal and Run kafka server

```shell
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties
```

Create a topic 

```shell
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092
```

Install the required Python packages:

```shell
pip install confluent_kafka pymongo
```

## Running producer
To run the Kafka producer, execute the following command:

```shell
python producer.py
```
The producer will start generating 10 million events and publish them to the Kafka topic.

## Running consumer

To run the Kafka consumer, execute the following command:

```shell
python consumer.py
```

The consumer will read the events from the Kafka topic and write them to MongoDB.


## Additional Notes

Make sure you have Apache Kafka and MongoDB properly installed and configured before running the producer and consumer scripts. Adjust the Kafka server properties and MongoDB connection details as needed in the respective scripts.

The producer.py and consumer.py files should be present in the same directory as this README.md file.
