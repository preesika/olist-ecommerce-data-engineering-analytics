-- =====================================================
-- Olist E-Commerce Business Analysis Queries
-- =====================================================


-- 1. Overall Sales KPIs
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(*) AS total_items,
    ROUND(SUM(price)::numeric, 2) AS product_revenue,
    ROUND(SUM(freight_value)::numeric, 2) AS freight_value,
    ROUND(SUM(total_order_item_value)::numeric, 2) AS total_value
FROM sales_analytics;


-- 2. Top 10 Product Categories by Revenue
SELECT
    product_category,
    ROUND(SUM(price)::numeric, 2) AS total_revenue
FROM sales_analytics
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 10;


-- 3. Product Revenue by Customer State
SELECT
    customer_state,
    ROUND(SUM(price)::numeric, 2) AS total_revenue
FROM sales_analytics
GROUP BY customer_state
ORDER BY total_revenue DESC;


-- 4. Monthly Product Revenue Trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(price)::numeric, 2) AS product_revenue
FROM sales_analytics
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;


-- 5. Orders by Status
SELECT
    order_status,
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_analytics
GROUP BY order_status
ORDER BY total_orders DESC;


-- 6. Orders by Payment Method
SELECT
    payment_type,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_value)::numeric, 2) AS total_payment_value
FROM payment_analytics
GROUP BY payment_type
ORDER BY total_payment_value DESC;


-- 7. Customer Review Score Distribution
SELECT
    review_score,
    COUNT(*) AS total_reviews
FROM review_analytics
GROUP BY review_score
ORDER BY review_score;


-- 8. Dataset Date Range
SELECT
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date
FROM sales_analytics;