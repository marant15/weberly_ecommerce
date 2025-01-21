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


## DB init

run sql:

```sql
  CREATE TABLE IF NOT EXISTS ecommerce.order_items
(
    order_item_id text COLLATE pg_catalog."default" NOT NULL,
    order_id text COLLATE pg_catalog."default",
    product_id text COLLATE pg_catalog."default",
    quantity integer,
    price double precision
)

TABLESPACE pg_default;
```

```sql
  CREATE TABLE IF NOT EXISTS ecommerce.orders
(
    order_id text COLLATE pg_catalog."default" NOT NULL,
    customer_id text COLLATE pg_catalog."default",
    order_date date,
    total_amount double precision,
    CONSTRAINT orders_pkey PRIMARY KEY (order_id)
)

TABLESPACE pg_default;
```

```sql
  CREATE TABLE IF NOT EXISTS ecommerce.products
(
    product_id text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default",
    category text COLLATE pg_catalog."default",
    price double precision
)

TABLESPACE pg_default;
```
