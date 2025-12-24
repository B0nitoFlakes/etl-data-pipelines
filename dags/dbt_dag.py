import os
from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig  # pyright: ignore[reportMissingImports]
from cosmos.profiles import SnowflakeUserPasswordProfileMapping  # pyright: ignore[reportMissingImports]

DBT_EXECUTABLE_PATH=f"{os.environ['AIRFLOW_HOME']}/ETLVenv/bin/dbt"

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database":"dbt_db", "schema":"dbt_schema"},
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_path="/usr/local/airflow/pipelines/dbt"),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE_PATH),
    schedule="30 8 1 * *",
    start_date=datetime(2025,12,23),
    catchup=False,
    dag_id="dbt_dag",
)