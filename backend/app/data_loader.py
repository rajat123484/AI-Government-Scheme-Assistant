import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# CSV path
CSV_PATH = BASE_DIR / "data" / "government_schemes.csv"

# Read the dataset once
df = pd.read_csv(CSV_PATH)

# Return all schemes
def get_all_schemes():
    return df.to_dict(orient="records")