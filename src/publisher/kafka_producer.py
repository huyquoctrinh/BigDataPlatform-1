from kafka import KafkaProducer,KafkaClient
import json
import time
import logging

class Producer:
    def __init__(self, 
        topic,
        kafka_broker = 'kafka:29092'
    ):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_broker
        )
        self.topic = topic

    def send(self, data):
        try:
            self.producer.send(self.topic, data)
            self.producer.flush()
        except Exception as e:
            logging.error('Failed to send data to Kafka')
            logging.error(e)