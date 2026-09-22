-- Olist E-Commerce Analytics
-- Analytics Views for Power BI


-- 1. Sales Analytics View
CREATE OR REPLACE VIEW sales_analytics AS
SELECT
    o.order_id,
    o.order_purchase_timestamp::timestamp AS order_date,
    o.order_status,

    c.customer_id,
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,

    oi.order_item_id,
    oi.product_id,
    oi.seller_id,

    COALESCE(
        t.product_category_name_english,
        p.product_category_name,
        'unknown'
    ) AS product_category,

    oi.price,
    oi.freight_value,
    (oi.price + oi.freight_value) AS total_order_item_value

FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
LEFT JOIN product_category_name_translation t
    ON p.product_category_name = t.product_category_name;


-- 2. Payment Analytics View
CREATE OR REPLACE VIEW payment_analytics AS
SELECT
    order_id,
    payment_type,
    payment_sequential,
    payment_installments,
    payment_value
FROM order_payments;


-- 3. Review Analytics View
CREATE OR REPLACE VIEW review_analytics AS
SELECT
    order_id,
    review_id,
    review_score,
    review_creation_date::timestamp AS review_date
FROM order_reviews;