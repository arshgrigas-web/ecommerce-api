import json

# Python dictionary
server_data = {
    "servers": [
        {"hostname": "node1", "ip": "192.168.3.100", "ram_gb": 48},
        {"hostname": "node2", "ip": "192.168.3.101", "ram_gb": 8},
        {"hostname": "node3", "ip": "192.168.3.102", "ram_gb": 32}
    ],
    "cluster": "production",
    "total_nodes": 3
}

# Write to JSON file
with open("servers.json", "w") as f:
    json.dump(server_data, f, indent=2)

print("JSON file written!")

# Read from JSON file
with open("servers.json", "r") as f:
    loaded_data = json.load(f)

print(f"Cluster: {loaded_data['cluster']}")
print(f"Total nodes: {loaded_data['total_nodes']}")
print("\nServers:")
for server in loaded_data['servers']:
    print(f"  {server['hostname']} - {server['ip']} - {server['ram_gb']}GB")