select pc.name, sum(quantity) quantity, sum(revenue) revenue
from ecommerce.daily_sales ds
JOIN ecommerce.products_clean pc ON ds.product_id = pc.product_id
group by 1 order by 3 desc;

select avg(total_amount)
FROM ecommerce.orders;

select category, sum(quantity) quantity, sum(revenue) revenue
from ecommerce.daily_sales
group by 1 order by 3 desc;

select order_date, sum(quantity) quantity, sum(revenue) revenue
from ecommerce.daily_sales
group by 1 order by 1 asc;