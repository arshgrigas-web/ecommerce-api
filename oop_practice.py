# 1. Product class first
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def display(self):
        print(f"Product: {self.name}")
        print(f"  Price: ${self.price}")
        print(f"  Stock: {self.stock} units")
    
    def apply_discount(self, percent):
        old_price = self.price
        self.price = self.price * (1 - percent/100)
        print(f"  Discount applied: ${old_price} → ${self.price:.2f}")
    
    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"  Sold {quantity} units. Remaining: {self.stock}")
        else:
            print(f"  Not enough stock! Only {self.stock} available")

# 2. User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []
    
    def display(self):
        print(f"User: {self.name} ({self.email})")
        print(f"  Total orders: {len(self.orders)}")

# 3. Order class
class Order:
    order_count = 0
    
    def __init__(self, user, product, quantity):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.user = user
        self.product = product
        self.quantity = quantity
        self.total = product.price * quantity
        user.orders.append(self)
    
    def display(self):
        print(f"Order #{self.order_id}")
        print(f"  Customer: {self.user.name}")
        print(f"  Product: {self.product.name}")
        print(f"  Quantity: {self.quantity}")
        print(f"  Total: ${self.total:.2f}")

# 4. Test code at the bottom
arshak = User("Arshak", "arshak@email.com")
laptop = Product("Laptop", 899.99, 7)

order1 = Order(arshak, laptop, 1)
order2 = Order(arshak, laptop, 2)

arshak.display()
print()
order1.display()
print()
order2.display()
print(f"\nTotal orders placed: {Order.order_count}")

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):  # override parent method
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

# In e-commerce context:
class DigitalProduct(Product):
    def __init__(self, name, price, download_url):
        super().__init__(name, price, stock=999)  # digital = unlimited stock
        self.download_url = download_url
    
    def display(self):
        super().display()  # call parent display
        print(f"  Download: {self.download_url}")

# Test
ebook = DigitalProduct("Python Guide", 29.99, "https://downloads.com/python-guide")
ebook.display()
ebook.sell(100)  # inherited from Product
ebook.display()