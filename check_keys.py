import pandas as pd

customers = pd.read_csv("data/olist_customers_dataset.csv")
orders = pd.read_csv("data/olist_orders_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
sellers = pd.read_csv("data/olist_sellers_dataset.csv")

print("===== CUSTOMERS =====")
print("customer_id unique:", customers["customer_id"].is_unique)

print("\n===== ORDERS =====")
print("order_id unique:", orders["order_id"].is_unique)
print("customer_id unique:", orders["customer_id"].is_unique)

print("\n===== PRODUCTS =====")
print("product_id unique:", products["product_id"].is_unique)

print("\n===== SELLERS =====")
print("seller_id unique:", sellers["seller_id"].is_unique)