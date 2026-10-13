import requests
import random
import time
import json

API = "http://ecommerce-api:8000"

USERS = [
    {"email": "bot_alice@shop.com", "username": "bot_alice", "password": "botpass123"},
    {"email": "bot_bob@shop.com", "username": "bot_bob", "password": "botpass123"},
    {"email": "bot_carol@shop.com", "username": "bot_carol", "password": "botpass123"},
    {"email": "bot_dave@shop.com", "username": "bot_dave", "password": "botpass123"},
    {"email": "bot_eve@shop.com", "username": "bot_eve", "password": "botpass123"},
]

ADDRESSES = [
    "Yerevan, Armenia",
    "Tbilisi, Georgia",
    "Paris, France",
    "Moscow, Russia",
    "Berlin, Germany",
]

def register_user(user):
    try:
        res = requests.post(f"{API}/auth/register", json=user, timeout=10)
        if res.status_code == 201:
            print(f"Registered: {user['username']}")
        elif res.status_code == 400:
            print(f"User exists: {user['username']}")
    except Exception as e:
        print(f"Register error: {e}")

def login_user(user):
    try:
        res = requests.post(f"{API}/auth/login", 
            json={"email": user["email"], "password": user["password"]}, 
            timeout=10)
        if res.status_code == 200:
            return res.json()["access_token"]
    except Exception as e:
        print(f"Login error: {e}")
    return None

def get_products():
    try:
        res = requests.get(f"{API}/products/", timeout=10)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"Products error: {e}")
    return []

def place_order(token, user_id, items, address):
    try:
        res = requests.post(
            f"{API}/orders/?user_id={user_id}",
            json={"items": items, "shipping_address": address},
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        if res.status_code == 201:
            order = res.json()
            print(f"Order placed: #{order['id']} - ${order['total_amount']:.2f}")
            return order
    except Exception as e:
        print(f"Order error: {e}")
    return None

def pay_order(order_id):
    try:
        res = requests.post(f"{API}/orders/{order_id}/pay", timeout=10)
        if res.status_code == 200:
            data = res.json()
            print(f"Payment for order #{order_id}: {data['message']}")
    except Exception as e:
        print(f"Payment error: {e}")

def run_bot():
    print("CustomerBot starting...")
    
    # Register all bot users
    for user in USERS:
        register_user(user)
        time.sleep(0.5)
    
    # Pick random user
    user = random.choice(USERS)
    print(f"\nBot acting as: {user['username']}")
    
    # Login
    token = login_user(user)
    if not token:
        print("Login failed!")
        return
    
    # Get products
    products = get_products()
    if not products:
        print("No products found!")
        return
    
    print(f"Found {len(products)} products")
    
    # Random shopping - pick 1-3 products
    num_items = random.randint(1, 3)
    selected = random.sample(products, min(num_items, len(products)))
    
    items = []
    for product in selected:
        quantity = random.randint(1, 3)
        items.append({"product_id": product["id"], "quantity": quantity})
        print(f"Adding to cart: {product['name']} x{quantity}")
    
    # Place order (use user_id 1 for now - will fix with proper auth later)
    address = random.choice(ADDRESSES)
    order = place_order(token, 1, items, address)
    
    if order:
        # Pay for order
        time.sleep(1)
        pay_order(order["id"])
    
    print("\nCustomerBot finished!")

if __name__ == "__main__":
    run_bot()