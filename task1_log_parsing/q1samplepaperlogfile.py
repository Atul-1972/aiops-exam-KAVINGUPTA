# Question 1 — AIOps Log Anomaly Detection
# You are working as an AIOps engineer for an application server. The server generates logs containing CPU usage, memory usage and response time.
# Create a Python program that:
# Creates or reads a sample dataset containing:
# Timestamp
# CPU Usage
# Memory Usage
# Response Time
# Calculates basic statistics for the metrics.
# Detects anomalous values using a simple threshold-based approach.
# Prints the anomalous records.
# Displays a graph showing the metric values and anomalies.
# Expected output:
# Total records: 20
# Anomalies detected: 3

# Timestamp       CPU       Status
# 10:05           95%      ANOMALY
# 10:12           97%      ANOMALY
# 10:18           92%      ANOMALY
# Concepts tested:
#  AIOps fundamentals, logs, metrics, anomaly detection.
import matplotlib.pyplot as plt

log = [
    "10:05,95,60,420ms",
    "10:45,90,70,230ms",
    "10:15,89,80,100ms",
    "10:00,74,61,560ms",
    "10:08,67,66,450ms",
    "10:01,99,69,310ms",
    "10:03,97,63,410ms",
    "10:04,93,65,460ms",
    "10:09,81,64,443ms",
    "10:10,92,60,434ms",
    "10:59,62,71,456ms",
    "10:42,72,78,450ms",
    "10:21,69,87,457ms",
    "10:31,105,80,460ms",
    "10:22,75,70,490ms",
    "10:23,65,64,500ms",
]

cpu=[]
error=0
normal=0
x=""
memeory_usage=[]
response_time=[]
for line in log:
    word=line.split(",")
    timestamp=word[0]
    cpu=word[1]
    memeory_usage=word[2]
    response_time=word[3]

    if cpu > "80":
        error=error+1
        x=x+timestamp + "           " + cpu + "%      ANOMALY\n"
    else:
        normal=normal+1

print("Total records: ",len(log))
print("Anomalies detected: ",error)

print("Timestamp       CPU       Status")
print(x)


import matplotlib.pyplot as plt

# CPU data jo logs mein hai
cpu = [95, 90, 89, 74, 67, 99, 97, 93, 81, 92, 62, 72, 69, 105, 75, 65]

# 1. CPU ki line
plt.plot(cpu, marker="o")

# 2. Red line 80 par (jisse upar wale anomalies saaf dikhein)
plt.axhline(80, color="red")

plt.show()