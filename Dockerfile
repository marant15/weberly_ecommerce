FROM apache/airflow:2.10.4-python3.8
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./airflow/airflow.cfg /opt/airflow/