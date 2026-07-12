SELECT *
FROM customer_sales;

SELECT
customer_state,
SUM(payment_value) AS revenue
FROM customer_sales
GROUP BY customer_state
ORDER BY revenue DESC;

SELECT
product_category_name,
SUM(payment_value) AS sales
FROM customer_sales
GROUP BY product_category_name
ORDER BY sales DESC
LIMIT 10;

SELECT
customer_unique_id,
SUM(payment_value) total_spent
FROM customer_sales
GROUP BY customer_unique_id
ORDER BY total_spent DESC
LIMIT 20;

SELECT
payment_type,
COUNT(*) transactions
FROM customer_sales
GROUP BY payment_type;