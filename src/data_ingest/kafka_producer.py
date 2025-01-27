from kafka import KafkaProducer,KafkaClient
import json
import time

class KafkaProducer:
    def __init__(self, 
        kafka_broker = 'localhost:9092', 
        topic
    ):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_broker
        )
        self.topic = topic

    def send(self, data):
        try:
            self.producer.send(self.topic, data)
        except Exception as e:
            print('Failed to send data to Kafka')
            print(e)