from kafka import KafkaProducer
import json
from django.http import HttpResponse




class CustomProducer:
    def __init__(self, servers):
        self.servers = servers
        self.producer = KafkaProducer(bootstrap_servers = servers)

    def send(topics, message):
        producer.send(topics, message)



producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
for __ in range (100):
    producer.send('foobar', b'some_message_bytes')

future = producer.send('foobar', b'another_message')
result = future.get(timeout = 60)

producer.flush()

producer.send('foobar', key = b'foo', value = b'bar')

producer = KafkaProducer(value_serializer = lambda v: json.dumps(v).encode('utf-8'))
producer.send('fizzbuzz', {'foo': 'bar'})

producer = KafkaProducer(key_serializer = str.encode)
producer.send('fliplap', key='ping', value =  '1234')

producer = KafkaProducer(compression_type = 'gzip')
for i in range(1000):
    producer.send('foobar', b'msg %d' %i)




