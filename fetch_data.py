import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")

headers = {
    "X-Auth-Token": API_KEY
}

BASE_URL = "https://api.football-data.org/v4/competitions/PL"

# --- Fetch standings ---
standings_res = requests.get(f"{BASE_URL}/standings", headers=headers)
standings_data = standings_res.json()

os.makedirs("data", exist_ok=True)

with open("data/standings.json", "w") as f:
    json.dump(standings_data, f, indent=2)

print("Standings saved")

# --- Fetch top scorers ---
scorers_res = requests.get(f"{BASE_URL}/scorers?limit=20", headers=headers)
scorers_data = scorers_res.json()

with open("data/scorers.json", "w") as f:
    json.dump(scorers_data, f, indent=2)

print("Scorers saved")