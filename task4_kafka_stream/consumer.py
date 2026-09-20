# Question 3 — Python Kafka Consumer
# Write a Python Kafka consumer that consumes messages from:
# server_metrics
# The consumer should:
# Connect to the Kafka broker.
# Subscribe to the server_metrics topic.
# Continuously receive messages.
# Display the received server metrics.
# Detect whether CPU usage is greater than 80%.
# Print:
# ALERT: High CPU detected on server01
# when the condition is satisfied.
# Example:
# Received:
# Server: server01
# CPU: 85%
# Memory: 62%

# ALERT: High CPU detected on server01
# Concepts tested:
# Concepts tested:
#  Consumer, topic, Python Kafka consumer, real-time monitoring, anomaly detection.

import json
from kafka import KafkaConsumer

consume=KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m:json.loads(m.decode("utf-8"))
)

for msg in consume:
    d=msg.value
    print("Received: ")
    print("Server: ",d["server_id"])
    print("CPU: ",d["cpu_usage"],"%")
    print("Memory: ",d["memory_usage"],"%")
    if d["cpu_usage"]>80:
        print("Alert:High cpu usage on",d["server_id"])


# Question 5 — Integrated AIOps Challenge
# Modify your Kafka consumer from Question 3 so that it behaves like a simple AIOps monitoring system.
# The consumer should:
# Receive server metrics from Kafka.
# Check CPU usage.
# Detect an anomaly when CPU > 80%.
# Print an alert.
# Maintain a count of detected anomalies.
# Example:
# Message received: server01 | CPU: 85%
# ALERT: High CPU detected

# Message received: server02 | CPU: 45%
# Normal

# Message received: server03 | CPU: 91%
# ALERT: High CPU detected

# Total anomalies detected: 2
# Concepts tested:
#  Kafka + Python + metrics + anomaly detection + AIOps monitoring.

#q5
# count = 0

# for msg in consume:
#     d = msg.value
#     print("Message received: ", d["server_id"], "| CPU: ", d["cpu_usage"], "%")
#     if d["cpu_usage"] > 80:
#         count = count + 1
#         print("Alert: High CPU detected")
#     else:
#         print("Normal")
#     print("Total anomalies detected: ", count)