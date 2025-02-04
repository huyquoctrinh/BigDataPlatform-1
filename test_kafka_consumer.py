import json
# from aiokafka import AIOKafkaConsumer
from kafka import KafkaConsumer
import asyncio
from json import loads
# from workers.db_handler import AtlasClient

class TestConsumer:
    def __init__(
        self, 
        topic,
        kafka_broker = 'localhost:9092', 
    ):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_broker,
            auto_offset_reset='earliest',
            value_deserializer=lambda m: loads(m.decode('utf-8'))
        )
        
    def consume(self):
        # while
        for message in self.consumer:
            # yield json.loads(message.value.decode('utf-8'))
            print(message)

consumer = TestConsumer(topic='test')
# print(next(consumer.consume()))
consumer.consume()