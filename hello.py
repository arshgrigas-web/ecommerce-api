# My first Python program
name = "Arshak"
age = 35

print(f"Hello, my name is {name}")
print(f"I am learning Python for DevOps")
print(f"2 + 2 = {2 + 2}")

# List example
skills = ["Linux", "Kubernetes", "Docker"]
print(f"My skills: {skills}")

for skill in skills:
    print(f"  - {skill}")

# Dictionary - like key:value pairs
server = {
    "hostname": "minisforumnode1",
    "ip": "192.168.3.100",
    "ram": "48GB",
    "os": "Ubuntu 26.04"
}

print(f"\nServer info:")
for key, value in server.items():
    print(f"  {key}: {value}")

# Functions
def check_server(hostname, ip, ram):
    print(f"\nChecking server: {hostname}")
    print(f"  IP: {ip}")
    print(f"  RAM: {ram}")
    if ram == "48GB":
        print(f"  Status: ✅ Sufficient RAM")
    else:
        print(f"  Status: ⚠️ Low RAM")

# Call the function
check_server("minisforumnode1", "192.168.3.100", "48GB")
check_server("node2", "192.168.3.101", "8GB")

# List of servers to check
servers = [
    {"hostname": "node1", "ip": "192.168.3.100", "ram": "48GB"},
    {"hostname": "node2", "ip": "192.168.3.101", "ram": "8GB"},
    {"hostname": "node3", "ip": "192.168.3.102", "ram": "32GB"},
]

print("\n=== Server Health Check ===")
for server in servers:
    check_server(server["hostname"], server["ip"], server["ram"])