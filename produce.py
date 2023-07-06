from confluent_kafka import Producer
from multiprocessing import Pool

def send_message(message):
    bootstrap_servers = 'localhost:9092'
    topic = 'news'
    
    # Create a Kafka producer instance
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    # Produce the message
    for i in range(1000000):
        producer.produce(topic, message)
        producer.flush()

if __name__ == '__main__':
    # Number of producers to send
    num_messages = 10
    
    # Number of worker processes to use
    num_workers = 8

    # Generate the messages to send
    messages = ['hello world'] * num_messages

    # Create a process pool with the specified number of workers
    pool = Pool(num_workers)

    # Use the process pool to send the messages in parallel
    pool.map(send_message, messages)

    # Close the process pool
    pool.close()
    pool.join()
