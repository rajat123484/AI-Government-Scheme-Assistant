import pandas as pd

# Load the CSV file
df = pd.read_csv("data/government_schemes.csv")

print("Dataset Loaded Successfully!")
print(df.head())

print("\nNumber of Schemes:", len(df))
print("Columns:")
print(df.columns)