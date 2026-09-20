# Question 2 — Kafka Topic and Producer
# Set up a Kafka environment and create a topic called:
# server_metrics
# Perform the following:
# Start the Kafka server/cluster.
# Create the server_metrics topic.
# Configure a Kafka producer.
# Send at least 10 server metric messages.
# Each message should contain:
# server_id
# cpu_usage
# memory_usage
# Example:
# {
#     "server_id": "server01",
#     "cpu_usage": 82,
#     "memory_usage": 65
# }
# Verify that the messages are successfully published to the topic.

#producer.py

import json
import time
from kafka import KafkaProducer

producer=KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:json.dumps(v).encode("utf-8")
)

log=[
    {"server_id": "server01", "cpu_usage": 82, "memory_usage": 65},
    {"server_id": "server02", "cpu_usage": 45, "memory_usage": 50},
    {"server_id": "server03", "cpu_usage": 91, "memory_usage": 70},
    {"server_id": "server04", "cpu_usage": 60, "memory_usage": 55},
    {"server_id": "server05", "cpu_usage": 85, "memory_usage": 62},
    {"server_id": "server06", "cpu_usage": 72, "memory_usage": 58},
    {"server_id": "server07", "cpu_usage": 95, "memory_usage": 80},
    {"server_id": "server08", "cpu_usage": 50, "memory_usage": 40},
    {"server_id": "server09", "cpu_usage": 88, "memory_usage": 75},
    {"server_id": "server10", "cpu_usage": 65, "memory_usage": 60}
]

for item in log:
    producer.send("server_metrics",item)
    print("Sent:",item)
    time.sleep(0.4)

producer.flush()
print("all 10 messages sent successfully")


