from kafka import KafkaProducer,KafkaClient
import json
import time


class TestProducer:
    def __init__(
        self, 
        topic,
        kafka_broker = 'localhost:9092', 
    ):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_broker
        )
        self.topic = topic
        # self.producer.topic(self.topic)
    def send(self, data):
        for i in range(100):
            self.producer.send(self.topic, data)
            self.producer.flush()
            # print('Message sent')

producer = TestProducer(topic='test')
producer.send(json.dumps({"results": "new text"}).encode('utf-8'))
