
import requests

url = "https://activity12-5-15e92-default-rtdb.firebaseio.com/.json"

print("Testing connection...")

response = requests.get(url, timeout=10)

print(response.status_code)
print(response.text)