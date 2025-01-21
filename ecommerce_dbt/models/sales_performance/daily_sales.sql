{{ config(materialized="table") }}

SELECT a.product_id, c.category, b.order_id, b.customer_id, b.order_date, a.quantity, a.price,
    a.quantity * a.price revenue
FROM {{ source('ecommerce', 'order_items') }} a
JOIN {{ source('ecommerce', 'orders') }} b ON a.order_id = b.order_id
JOIN {{ ref('products_clean') }} c ON c.product_id = a.product_id
