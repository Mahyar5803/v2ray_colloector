import requests
import base64

def fetch_configs():
    url = "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip().split('\n')
    return []

def save_subscription():
    configs = fetch_configs()
    encoded = base64.b64encode('\n'.join(configs).encode()).decode()
    with open("sub.txt", "w") as f:
        f.write(encoded)

save_subscription()
