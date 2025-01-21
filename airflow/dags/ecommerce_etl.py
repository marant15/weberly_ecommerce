from airflow import DAG
from pendulum import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator

load_postgres_sql = """BEGIN;
TRUNCATE ecommerce.{table};
\copy ecommerce.{table} FROM '/Users/marwin/projects/{table}.csv' (DELIMITER ',', ON_ERROR ignore, FORMAT CSV, HEADER true);
COMMIT;
"""
enter_postgres_db = "export PGPASSWORD='admin'; /usr/local/bin/psql -U 'postgres' -d 'ecommerce' << EOF"
load_ecommerce_command = enter_postgres_db + load_postgres_sql.format(table="products") + \
    load_postgres_sql.format(table="orders") + load_postgres_sql.format(table="order_items") + \
    "EOF"
run_sbt_command = """source airflow-env/bin/activate
cd projects/ecommerce/ecommerce_dbt
{dbt_command}"""

dag = DAG(
    dag_id="ecommerce_sales_summary",
    start_date=datetime(2025,1,1),
    catchup=False,
    schedule_interval="@daily"
)

load_ecommerce_data = SSHOperator(
    task_id='load_ecommerce_data',
    ssh_conn_id='my_ssh_connection',
    command=load_ecommerce_command,
    dag=dag
)

run_ecommerce_data_tests = SSHOperator(
    task_id='run_ecommerce_data_tests',
    ssh_conn_id='my_ssh_connection',
    command=run_sbt_command.format(dbt_command='dbt test --select "source*"'),
    dag=dag
)

cleanup_product_data = SSHOperator(
    task_id='cleanup_product_data',
    ssh_conn_id='my_ssh_connection',
    command=run_sbt_command.format(dbt_command='dbt run --select "products_clean"'),
    dag=dag
)

test_cleanned_product_data = SSHOperator(
    task_id='test_cleanned_product_data',
    ssh_conn_id='my_ssh_connection',
    command=run_sbt_command.format(dbt_command='dbt test --select "sales_performance"'),
    dag=dag
)

generate_sales_summaries = SSHOperator(
    task_id='generate_sales_summaries',
    ssh_conn_id='my_ssh_connection',
    command=run_sbt_command.format(dbt_command='dbt run --select "daily_sales"'),
    dag=dag
)

load_ecommerce_data >> run_ecommerce_data_tests >> cleanup_product_data
cleanup_product_data >> test_cleanned_product_data >> generate_sales_summaries
