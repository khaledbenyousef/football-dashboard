import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/competitions/PL/standings"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)

data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/standings.json", "w") as f:
    json.dump(data, f, indent=2)

print("Done! Data saved to data/standings.json")