# Writing to a file
with open("servers.txt", "w") as f:
    f.write("node1,192.168.3.100,48GB\n")
    f.write("node2,192.168.3.101,8GB\n")
    f.write("node3,192.168.3.102,32GB\n")

print("File written!")

# Reading from a file
with open("servers.txt", "r") as f:
    content = f.read()
    print("File contents:")
    print(content)

# Reading line by line
print("Line by line:")
with open("servers.txt", "r") as f:
    for line in f:
        line = line.strip()  # remove newline character
        parts = line.split(",")  # split by comma
        hostname = parts[0]
        ip = parts[1]
        ram = parts[2]
        print(f"  {hostname} → {ip} → {ram}")