# Without error handling - crashes!
# print(10 / 0)  # ZeroDivisionError

# With error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Real DevOps example - reading a file that might not exist
try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found! Creating default config...")
    with open("missing_file.txt", "w") as f:
        f.write("default config")
    print("Default config created!")

# Multiple exceptions
def read_server_config(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Config file {filename} not found!")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

import json
result = read_server_config("servers.json")
if result:
    print(f"Loaded config: {result['cluster']}")

result2 = read_server_config("nonexistent.json")
print(f"Result2: {result2}")