from airflow import DAG
from datetime import datetime
from airflow.operators.python_ import PythonOperator

def collect_data():
    print("Collecting data...")
    print("CPU USAGE: 45%")
    print("MEMORY USAGE: 60%")
    print("ERROR _RATE: 0.5%")

def process_data():
    print("Processing the data......")

def detect_anomalies():
    CPU=70
    if CPU>80:
        print("ALERT: CPU usage is above the threshold!")
    else:
        print("CPU usage is within the threshold.")

def saving_results():
    print("Saving the results in the database......")

with DAG(
    dag_id="practical2ai_ops.dag",
    start_date=datetime(2026,9,14),
    schedule=None,
    catchup=False
) as dag:
    
    collect_data_task=PythonOperator(
        task_id="collect_data",
        python_callable=collect_data,
    )
    process_data_task=PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    detect_anomalies_task=PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies,
    )

    saving_results_task=PythonOperator(
        task_id="saving_results",
        python_callable=saving_results,
    )

    collect_data_task >> process_data_task >> detect_anomalies_task >> saving_results_task



