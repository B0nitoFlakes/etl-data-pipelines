from airflow import DAG  # pyright: ignore[reportMissingImports]
from airflow.operators.python import PythonOperator  # pyright: ignore[reportMissingImports]
from datetime import datetime
from pipelines.src.raw_products import task

with DAG(
    dag_id="raw_products_dag",
    start_date=datetime(2025, 12, 24),
    schedule="0 9 1 * *",
    catchup=False,
    tags=["test"]
) as dag:

    fetch_raw_data = PythonOperator(
        task_id="fetch_raw_products_data",
        python_callable=task
    )