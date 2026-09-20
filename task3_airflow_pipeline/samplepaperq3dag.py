# Question 4 — Build an AIOps Workflow using Airflow
# Create an Apache Airflow DAG representing a basic AIOps workflow.
# The workflow should contain the following tasks:
# Collect Metrics
#       ↓
# Process Metrics
#       ↓
# Detect Anomaly
#       ↓
# Generate Report
# Requirements
# Task 1 — collect_metrics
# Use PythonOperator to generate/sample server metrics.
# Example:
# CPU = 87
# Memory = 65
# Response Time = 420ms
# Task 2 — process_metrics
# Process the collected metrics and print them.
# Task 3 — detect_anomaly
# Check whether:
# CPU > 80
# If yes, print:
# Anomaly detected: High CPU usage
# Otherwise:
# No anomaly detected
# Task 4 — generate_report
# Print a final AIOps report:
# ===== AIOps Report =====
# Metrics collected successfully
# Metrics processed successfully
# Anomaly detection completed
# ========================
# DAG Requirements
# Your DAG must:
# Use PythonOperator.
# Define all four tasks.
# Define the correct dependencies.
# Run the tasks in the following order:
# collect_metrics >> process_metrics >> detect_anomaly >> generate_report
# Concepts tested:
#  Airflow, DAG, PythonOperator, dependencies, AIOps lifecycle, basic AIOps workflow.



from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def collect_metrics_task():
    print("CPU=87")
    print("Memory=65")
    print("ResponseTime=420ms")


def proccess_metrics_task():
    print("metrics are collected and are being processed")


def detect_anomalies_task():
    CPU = 87
    if CPU > 80:
        print("Anomaly detected:High CPU USAGE")
    else:
        print("No anomaly detected")


def generate_report_task():
    print("===== AIOps Report =====")
    print("Metrics collected successfully")
    print("Metrics processed successfully")
    print("Anomaly detection completed")


with DAG(
    dag_id="aiops_task",
    catchup=False,
    schedule=None,
    start_date=datetime(2026, 9, 14),
) as dag:

    collect_metrics = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics_task,
    )

    process_metrics = PythonOperator(
        task_id="process_metrics",
        python_callable=proccess_metrics_task,
    )

    detect_anomalies = PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies_task,
    )

    generate_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report_task,
    )

    collect_metrics >> process_metrics >> detect_anomalies >> generate_report
