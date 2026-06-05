from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_download():
    exec(open('/mnt/d/CDF/Automate a Data Processing Task with Apache Airflow/airflow-data-pipeline/scripts/download_data.py').read())

def run_process():
    exec(open('/mnt/d/CDF/Automate a Data Processing Task with Apache Airflow/airflow-data-pipeline/scripts/process_data.py').read())

def run_summarize():
    exec(open('/mnt/d/CDF/Automate a Data Processing Task with Apache Airflow/airflow-data-pipeline/scripts/summarize_data.py').read())

with DAG(
    'iris_data_pipeline',
    default_args=default_args,
    description='A simple Iris data processing pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    download_task = PythonOperator(
        task_id='download_data',
        python_callable=run_download,
    )

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=run_process,
    )

    summarize_task = PythonOperator(
        task_id='summarize_data',
        python_callable=run_summarize,
    )

    download_task >> process_task >> summarize_task
