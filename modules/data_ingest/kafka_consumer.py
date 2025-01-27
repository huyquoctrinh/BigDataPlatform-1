from kafka import KafkaConsumer
import json

class KafkaConsumer:
    def __init__(self, 
        kafka_broker = 'localhost:9092', 
        topic
    ):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_broker,
            auto_offset_reset='earliest',
            group_id='consumer-group-1'
        )
        self.topic = topic

    def consume(self):
        for message in self.consumer:
            yield json.loads(message.value.decode('utf-8'))