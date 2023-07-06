from confluent_kafka import Consumer, KafkaException
from pymongo import MongoClient

# Kafka configuration
bootstrap_servers = 'localhost:9092'
group_id = 'my-consumer-group'
topic = 'news'

# MongoDB configuration
mongo_uri = 'mongodb://localhost:27017'
mongo_db = 'mydatabase'
mongo_collection = 'messages'

def consume_and_store_message():
    # Create a Kafka consumer instance
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    })

    # Create a MongoDB client
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]

    # Subscribe to the Kafka topic
    consumer.subscribe([topic])

    try:
        while True:
            # Poll for new Kafka messages
            message = consumer.poll(1.0)

            if message is None:
                continue
            elif message.error():
                if message.error().code() == KafkaException._PARTITION_EOF:
                    # Reached the end of the partition
                    print(f'{topic} [{message.partition()}] reached end at offset {message.offset()}\n')
                else:
                    # Raise KafkaException for other errors
                    raise KafkaException(message.error())
            else:
                # Store the message in MongoDB
                msg_value = message.value().decode('utf-8')
                collection.insert_one({'message': msg_value})
                print(f'Message stored in MongoDB: {msg_value}')

    except KeyboardInterrupt:
        # Gracefully stop the consumer on keyboard interrupt
        print('Keyboard interrupt detected. Stopping consumer...\n')

    finally:
        # Close the Kafka consumer and MongoDB client
        consumer.close()
        client.close()

if __name__ == '__main__':
    consume_and_store_message()
