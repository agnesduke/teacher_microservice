from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json
from django.http import HttpResponse
from typing import List, Any

# Set your Kafka bootstrap servers
bootstrap_servers = "localhost:9092"


class CustomProducer:
    def __init__(self, servers: List[str] | str,**configs: Any):
        self.servers = servers
        self.producer = KafkaProducer(bootstrap_servers=servers,**configs)

    def send(
        self,
        topic: Any,
        value: Any | None = None,
        key: Any | None = None,
        headers: Any | None = None,
        partition: Any | None = None,
        timestamp_ms: Any | None = None,
    ):
        self.create_topic(topic)
        self.producer.send(topic, value, key, headers, partition, timestamp_ms)


    def create_topic(self, topic):
        admin_client = KafkaAdminClient(bootstrap_servers=self.servers)
        topic_metadata = admin_client.list_topics()
        if topic not in topic_metadata:
            admin_client.create_topics(
                [NewTopic(name=topic, num_partitions=1, replication_factor=1)]
            )
            print("Topic created : ", topic)

    def flush(self,timeout: Any | None = None):
        self.producer.flush(timeout)

    def close(self):
        self.producer.close()

    def __del__(self):
        self.producer.close()


# producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
# for __ in range(100):
#     producer.send("foobar", b"some_message_bytes")

producer = CustomProducer(servers=bootstrap_servers)

for __ in range(10):
    producer.send("foobar", b"some_message_bytes")
    print("Message sent")

producer.flush()


# future = producer.send("foobar", b"another_message")
# result = future.get(timeout=60)

# producer.flush()

# producer.send("foobar", key=b"foo", value=b"bar")

# producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode("utf-8"))
# producer.send("fizzbuzz", {"foo": "bar"})

# producer = KafkaProducer(key_serializer=str.encode)
# producer.send("fliplap", key="ping", value="1234")

# producer = KafkaProducer(compression_type="gzip")
# for i in range(1000):
#     producer.send("foobar", b"msg %d" % i)
