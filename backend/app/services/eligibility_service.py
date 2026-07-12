import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
SCHEMES_FILE = BASE_DIR / "data" / "schemes.json"

def check_eligibility(profile):
    with open(SCHEMES_FILE, "r", encoding="utf-8") as file:
        schemes_data = json.load(file)

    eligible = []

    for scheme in schemes_data:
        if scheme.get("occupation") == profile.occupation:
            eligible.append(scheme)

        elif "max_income" in scheme and profile.income <= scheme["max_income"]:
            eligible.append(scheme)

        elif "category" in scheme and profile.category in scheme["category"]:
            eligible.append(scheme)

    return eligible