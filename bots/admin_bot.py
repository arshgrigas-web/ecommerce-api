import requests
import random
import time

API = "http://ecommerce-api:8000"

def get_orders(user_id=1):
    try:
        res = requests.get(f"{API}/orders/?user_id={user_id}", timeout=10)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"Error getting orders: {e}")
    return []

def update_order_status(order_id, status):
    try:
        res = requests.put(
            f"{API}/orders/{order_id}/status?status={status}",
            timeout=10
        )
        if res.status_code == 200:
            print(f"Order #{order_id} → {status}")
            return True
        else:
            print(f"Failed to update order #{order_id}: {res.text}")
    except Exception as e:
        print(f"Error updating order {order_id}: {e}")
    return False

def restock_product(product_id, add_stock=50):
    try:
        # Get current product
        res = requests.get(f"{API}/products/{product_id}", timeout=10)
        if res.status_code != 200:
            return
        product = res.json()
        
        new_stock = product["stock"] + add_stock
        res = requests.put(
            f"{API}/products/{product_id}",
            json={"stock": new_stock},
            timeout=10
        )
        if res.status_code == 200:
            print(f"Restocked product #{product_id} '{product['name']}': {product['stock']} → {new_stock}")
    except Exception as e:
        print(f"Error restocking product {product_id}: {e}")

def check_low_stock():
    try:
        res = requests.get(f"{API}/products/", timeout=10)
        if res.status_code == 200:
            products = res.json()
            low_stock = [p for p in products if p["stock"] < 10]
            return low_stock
    except Exception as e:
        print(f"Error checking stock: {e}")
    return []

def run_bot():
    print("AdminBot starting...")
    
    # Get all orders for user 1 (our test user)
    orders = get_orders(user_id=1)
    print(f"Found {len(orders)} total orders")
    
    # Process pending orders - mark as processing
    pending = [o for o in orders if o["status"] == "pending" and o["payment_status"] == "success"]
    print(f"Pending paid orders: {len(pending)}")
    
    for order in pending:
        print(f"Processing order #{order['id']} - ${order['total_amount']:.2f}")
        update_order_status(order["id"], "processing")
        time.sleep(0.5)
    
    # Check low stock and restock
    low_stock = check_low_stock()
    if low_stock:
        print(f"\nLow stock alert! {len(low_stock)} products need restocking:")
        for product in low_stock:
            print(f"  - {product['name']}: {product['stock']} left")
            restock_product(product["id"], add_stock=100)
            time.sleep(0.5)
    else:
        print("\nAll products have sufficient stock")
    
    print("\nAdminBot finished!")

if __name__ == "__main__":
    run_bot()