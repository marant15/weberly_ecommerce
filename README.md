# Weberly ecommerce

This app shows how to implement an orchestration software, in this case airflow, to manage a simple ETL in postgres.

It uses DBT to do the transformation and testing.


## Build airflow

To run airflow, we have:

```bash
  docker build -t ecommerce/airflow .
  docker-compose up postgres
  docker-compose up initdb 
  docker-compose up webserver scheduler
```


## Documentation

To generate DBT documentation:

```bash
  dbt docs generate
  dbt docs serve
```
