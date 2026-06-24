import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# NAV must be positive
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Saved successfully.")