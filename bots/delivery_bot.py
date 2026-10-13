import requests
import random
import time

API = "http://ecommerce-api:8000"

def get_orders_by_status(status):
    try:
        # Get orders - we'll check all user IDs 1-100
        orders = []
        res = requests.get(f"{API}/orders/?user_id=1", timeout=10)
        if res.status_code == 200:
            all_orders = res.json()
            orders = [o for o in all_orders if o["status"] == status]
        return orders
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
    except Exception as e:
        print(f"Error updating order {order_id}: {e}")
    return False

def run_bot():
    print("DeliveryBot starting...")
    
    # Move processing orders to shipped
    processing_orders = get_orders_by_status("processing")
    print(f"Found {len(processing_orders)} processing orders")
    
    for order in processing_orders:
        # 70% chance to ship each order
        if random.random() > 0.3:
            update_order_status(order["id"], "shipped")
            time.sleep(0.5)
    
    # Move shipped orders to delivered
    shipped_orders = get_orders_by_status("shipped")
    print(f"Found {len(shipped_orders)} shipped orders")
    
    for order in shipped_orders:
        # 50% chance to deliver each order
        if random.random() > 0.5:
            update_order_status(order["id"], "delivered")
            time.sleep(0.5)
    
    print("DeliveryBot finished!")

if __name__ == "__main__":
    run_bot()