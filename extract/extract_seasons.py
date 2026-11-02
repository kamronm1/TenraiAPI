import json
import os
import time

import requests

BASE_URL = "https://api.tenrai.org/v1"
YEAR = 2026
SEASONS = ["winter", "spring", "summer", "fall"]
OUTPUT_DIR = "data/raw"


def fetch_season(year, season):
    page = 1
    all_anime = []

    while True:
        url = f"{BASE_URL}/seasons/{year}/{season}?page={page}"
        response = requests.get(url, timeout=10)
        data = response.json()

        all_anime.extend(data["data"])
        print(f"{season} page {page}: fetched {len(data['data'])}, total so far {len(all_anime)}")

        if not data["pagination"]["has_next_page"]:
            break

        page += 1
        time.sleep(1)

    return all_anime


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


os.makedirs(OUTPUT_DIR, exist_ok=True)

for season in SEASONS:
    anime_list = fetch_season(YEAR, season)
    path = f"{OUTPUT_DIR}/anime_{YEAR}_{season}.json"
    save_json(anime_list, path)
    print(f"saved {len(anime_list)} anime to {path}\n")
    time.sleep(1)

print("done")