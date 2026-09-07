import requests
import json
import urllib3

# Suppress SSL warning for development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def make_request(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # raises error if status != 200
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Connection error - check internet!")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None

# Test it
data = make_request("https://api.github.com")
print(f"GitHub API status: OK")
print(f"Current user URL: {data['current_user_url']}")

# Get public repos list
repos = make_request("https://api.github.com/users/torvalds/repos")
if repos:
    print(f"\nLinus Torvalds has {len(repos)} public repos:")
    for repo in repos[:5]:
        print(f"  - {repo['name']}: {repo['description']}")