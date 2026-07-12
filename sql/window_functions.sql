WITH customer_revenue AS
(
SELECT
customer_unique_id,
SUM(payment_value) revenue
FROM customer_sales
GROUP BY customer_unique_id
)

SELECT *,
RANK() OVER(ORDER BY revenue DESC) customer_rank
FROM customer_revenue;

WITH state_sales AS
(
SELECT
customer_state,
SUM(payment_value) revenue
FROM customer_sales
GROUP BY customer_state
)

SELECT *,
DENSE_RANK() OVER(ORDER BY revenue DESC) state_rank
FROM state_sales;

SELECT
customer_unique_id,
payment_value,
ROW_NUMBER() OVER(
PARTITION BY customer_unique_id
ORDER BY payment_value DESC
) rn
FROM customer_sales;