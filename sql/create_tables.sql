create table customers(
customer_id VARCHAR(50),
customer_unique_id VARCHAR(50),
customer_zip_code_prefix INT,
customer_city VARCHAR(100),
customer_state CHAR(2)
);
create table orders(
order_id VARCHAR(50),
customer_id VARCHAR(50),
order_status VARCHAR(30),
order_purchase_timestamp DATETIME
);

create table payments(
order_id VARCHAR(50),
payment_sequential INT,
payment_type VARCHAR(30),
payment_installments INT,
payment_value FLOAT
);

create table products(
product_id VARCHAR(50),
product_category_name VARCHAR(100)
);
