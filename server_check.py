def check_server(hostname, ip, ram_gb):
    print(f"\nChecking server: {hostname}")
    print(f"  IP: {ip}")
    print(f"  RAM: {ram_gb}GB")
    
    if ram_gb >= 32:
        status = "✅ Sufficient"
    elif ram_gb >= 16:
        status = "⚠️ Acceptable"
    else:
        status = "❌ Low RAM"
    
    print(f"  Status: {status}")
    return status

servers = [
    {"hostname": "node1", "ip": "192.168.3.100", "ram_gb": 48},
    {"hostname": "node2", "ip": "192.168.3.101", "ram_gb": 8},
    {"hostname": "node3", "ip": "192.168.3.102", "ram_gb": 32},
]

print("=== Server Health Check ===")
results = []
for server in servers:
    status = check_server(server["hostname"], server["ip"], server["ram_gb"])
    results.append({"hostname": server["hostname"], "status": status})

print("\n=== Summary ===")
for result in results:
    print(f"  {result['hostname']}: {result['status']}")