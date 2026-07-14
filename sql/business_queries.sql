select *
from customer_sales;

select
    customer_state,
    sum(payment_value) as revenue
from customer_sales
group by customer_state
order by revenue desc;

select
    product_category_name,
    sum(payment_value) as sales
from customer_sales
group by product_category_name
order by sales desc
limit 10;

select
    customer_unique_id,
    sum(payment_value) as total_spent
from customer_sales
group by customer_unique_id
order by total_spent desc
limit 20;

select
    payment_type,
    count(*) as transactions
from customer_sales
group by payment_type;
